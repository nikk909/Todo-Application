"""
FastAPI 后端 - 待办事项应用
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from contextlib import asynccontextmanager
import sqlite3
from datetime import datetime
import os

# 数据库配置
DB_PATH = os.path.join(os.path.dirname(__file__), "todos.db")


# 初始化数据库
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
    
    conn.commit()
    conn.close()


# Lifespan 事件管理
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    init_db()
    print(f"✅ 数据库已初始化: {DB_PATH}")
    yield
    # 关闭时执行（如果需要）
    print("👋 应用关闭")


# 创建 FastAPI 应用
app = FastAPI(title="待办事项 API", version="1.0.0", lifespan=lifespan)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic 模型
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


# 数据库连接
def get_db():
    # check_same_thread=False 允许跨线程使用连接（FastAPI 异步需要）
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


# ==================== API 路由 ====================


@app.get("/")
async def root():
    """健康检查"""
    return {"message": "待办事项 API 服务正常运行", "version": "1.0.0"}


@app.get("/api/todos", response_model=List[Todo])
async def get_todos(
    filter: Optional[str] = None,
    conn: sqlite3.Connection = Depends(get_db)
):
    """
    获取所有待办事项
    - filter: 筛选条件 (all/active/completed)
    """
    cursor = conn.cursor()
    
    if filter == "active":
        cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE completed = 0 ORDER BY created_at DESC")
    elif filter == "completed":
        cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE completed = 1 ORDER BY created_at DESC")
    else:
        cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos ORDER BY created_at DESC")
    
    rows = cursor.fetchall()
    # 转换 completed 从整数到布尔值
    return [{**dict(row), 'completed': bool(row['completed'])} for row in rows]


@app.get("/api/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int, conn: sqlite3.Connection = Depends(get_db)):
    """获取单个待办事项"""
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    
    if not row:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    
    result = dict(row)
    result['completed'] = bool(result['completed'])
    return result


@app.post("/api/todos", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate, conn: sqlite3.Connection = Depends(get_db)):
    """创建新的待办事项"""
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
    """更新待办事项"""
    cursor = conn.cursor()
    
    # 检查是否存在
    cursor.execute("SELECT id FROM todos WHERE id = ?", (todo_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="待办事项不存在")
    
    # 更新字段
    update_fields = []
    params = []
    
    if todo.text is not None:
        update_fields.append("text = ?")
        params.append(todo.text)
    
    if todo.completed is not None:
        update_fields.append("completed = ?")
        params.append(1 if todo.completed else 0)
    
    if update_fields:
        update_fields.append("updated_at = ?")
        params.append(datetime.now().isoformat())
        params.append(todo_id)
        
        cursor.execute(
            f"UPDATE todos SET {', '.join(update_fields)} WHERE id = ?",
            params
        )
        conn.commit()
    
    # 返回更新后的数据
    cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    
    result = dict(row)
    result['completed'] = bool(result['completed'])
    return result


@app.delete("/api/todos/{todo_id}")
async def delete_todo(todo_id: int, conn: sqlite3.Connection = Depends(get_db)):
    """删除单个待办事项"""
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="待办事项不存在")
    
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    
    return {"message": "删除成功", "id": todo_id}


@app.delete("/api/todos/clear/completed")
async def clear_completed(conn: sqlite3.Connection = Depends(get_db)):
    """清除所有已完成的待办事项"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE completed = 1")
    deleted_count = cursor.rowcount
    conn.commit()
    
    return {"message": "已清除所有已完成任务", "count": deleted_count}


@app.delete("/api/todos/clear/all")
async def clear_all(conn: sqlite3.Connection = Depends(get_db)):
    """清空所有待办事项"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos")
    deleted_count = cursor.rowcount
    conn.commit()
    
    return {"message": "已清空所有任务", "count": deleted_count}


@app.get("/api/stats")
async def get_stats(conn: sqlite3.Connection = Depends(get_db)):
    """获取统计信息"""
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as total FROM todos")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) as completed FROM todos WHERE completed = 1")
    completed = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) as active FROM todos WHERE completed = 0")
    active = cursor.fetchone()[0]
    
    return {
        "total": total,
        "completed": completed,
        "active": active
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

