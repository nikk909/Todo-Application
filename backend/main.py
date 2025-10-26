"""
FastAPI Backend - Todo Application with Search and Pagination
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Dict, Any
from contextlib import asynccontextmanager
import sqlite3
from datetime import datetime
import os

# Database configuration
DB_PATH = os.path.join(os.path.dirname(__file__), "todos.db")


# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_todos_completed ON todos(completed)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_todos_created_at ON todos(created_at DESC)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_todos_text ON todos(text)")
    
    conn.commit()
    conn.close()


# Lifespan event management
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    print(f"Database initialized: {DB_PATH}")
    yield
    # Shutdown
    print("Application closing")


# Create FastAPI application
app = FastAPI(title="Todo API", version="2.0.0", lifespan=lifespan)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models
class TodoCreate(BaseModel):
    text: str


class TodoUpdate(BaseModel):
    text: Optional[str] = None
    completed: Optional[bool] = None


class Todo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    text: str
    completed: bool
    created_at: str
    updated_at: str


class PaginatedTodos(BaseModel):
    todos: List[Todo]
    total: int
    page: int
    page_size: int
    total_pages: int


# Database connection
def get_db():
    # check_same_thread=False allows cross-thread connection usage (needed for FastAPI async)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


# ==================== API Routes ====================


@app.get("/")
async def root():
    """Health check"""
    return {"message": "Todo API Service Running", "version": "2.0.0"}


@app.get("/api/todos")
async def get_todos(
    filter: Optional[str] = "all",
    search: Optional[str] = None,
    search_type: Optional[str] = "fuzzy",  # fuzzy or exact
    page: Optional[int] = 1,
    page_size: Optional[int] = 10,
    conn: sqlite3.Connection = Depends(get_db)
) -> Dict[str, Any]:
    """
    Get todo list with search and pagination
    
    - **filter**: all (all), active (incomplete), completed (completed)
    - **search**: search keyword
    - **search_type**: fuzzy (fuzzy search) or exact (exact search)
    - **page**: page number (starts from 1)
    - **page_size**: items per page (0 = no pagination)
    """
    cursor = conn.cursor()
    
    # Build base query
    query = "SELECT id, text, completed, created_at, updated_at FROM todos WHERE 1=1"
    params = []
    
    # Add filter condition
    if filter == "active":
        query += " AND completed = 0"
    elif filter == "completed":
        query += " AND completed = 1"
    
    # Add search condition
    if search and search.strip():
        if search_type == "exact":
            query += " AND text = ?"
            params.append(search.strip())
        else:  # fuzzy search
            query += " AND text LIKE ?"
            params.append(f"%{search.strip()}%")
    
    # Get total count (for pagination)
    count_query = query.replace("SELECT id, text, completed, created_at, updated_at", "SELECT COUNT(*)")
    cursor.execute(count_query, params)
    total = cursor.fetchone()[0]
    
    # Add sorting
    query += " ORDER BY created_at DESC"
    
    # Add pagination
    total_pages = 1
    if page_size and page_size > 0:
        offset = (page - 1) * page_size
        query += f" LIMIT ? OFFSET ?"
        params.extend([page_size, offset])
        total_pages = (total + page_size - 1) // page_size if total > 0 else 1
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    # Convert completed to boolean
    todos = [{**dict(row), 'completed': bool(row['completed'])} for row in rows]
    
    # Return pagination info
    return {
        "todos": todos,
        "total": total,
        "page": page,
        "page_size": page_size if page_size > 0 else total,
        "total_pages": total_pages
    }


@app.get("/api/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int, conn: sqlite3.Connection = Depends(get_db)):
    """Get single todo"""
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    
    if not row:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    result = dict(row)
    result['completed'] = bool(result['completed'])
    return result


@app.post("/api/todos", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate, conn: sqlite3.Connection = Depends(get_db)):
    """Create new todo"""
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    
    cursor.execute(
        "INSERT INTO todos (text, completed, created_at, updated_at) VALUES (?, 0, ?, ?)",
        (todo.text, now, now)
    )
    conn.commit()
    
    todo_id = cursor.lastrowid
    cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    
    result = dict(row)
    result['completed'] = bool(result['completed'])
    return result


@app.put("/api/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    conn: sqlite3.Connection = Depends(get_db)
):
    """Update todo"""
    cursor = conn.cursor()
    
    # Check if todo exists
    cursor.execute("SELECT id FROM todos WHERE id = ?", (todo_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Build update query
    updates = []
    params = []
    
    if todo.text is not None:
        updates.append("text = ?")
        params.append(todo.text)
    
    if todo.completed is not None:
        updates.append("completed = ?")
        params.append(int(todo.completed))
    
    if not updates:
        # No updates provided, return current todo
        cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE id = ?", (todo_id,))
        row = cursor.fetchone()
        result = dict(row)
        result['completed'] = bool(result['completed'])
        return result
    
    # Add updated_at
    updates.append("updated_at = ?")
    params.append(datetime.now().isoformat())
    params.append(todo_id)
    
    query = f"UPDATE todos SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query, params)
    conn.commit()
    
    # Return updated todo
    cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    
    result = dict(row)
    result['completed'] = bool(result['completed'])
    return result


@app.delete("/api/todos/{todo_id}")
async def delete_todo(todo_id: int, conn: sqlite3.Connection = Depends(get_db)):
    """Delete todo"""
    cursor = conn.cursor()
    
    # Check if exists
    cursor.execute("SELECT id FROM todos WHERE id = ?", (todo_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Todo not found")
    
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    
    return {"message": "Delete successful", "id": todo_id}


@app.delete("/api/todos/clear/completed")
async def clear_completed_todos(conn: sqlite3.Connection = Depends(get_db)):
    """Clear all completed todos"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE completed = 1")
    conn.commit()
    
    return {"message": "Cleared all completed tasks", "count": cursor.rowcount}


@app.delete("/api/todos/clear/all")
async def clear_all_todos(conn: sqlite3.Connection = Depends(get_db)):
    """Clear all todos"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos")
    conn.commit()
    
    return {"message": "Cleared all tasks", "count": cursor.rowcount}


@app.get("/api/stats")
async def get_stats(conn: sqlite3.Connection = Depends(get_db)):
    """Get todo statistics"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed,
            SUM(CASE WHEN completed = 0 THEN 1 ELSE 0 END) as active
        FROM todos
    """)
    stats = cursor.fetchone()
    return dict(stats)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
