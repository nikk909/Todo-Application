# ✨ Advanced Todo Manager 📝

A powerful full-stack todo application built with React + FastAPI + SQLite, featuring advanced search, pagination, inline editing, and a stunning animated UI.

## 🚀 Features

### Core Functionality
- ✅ **Add Tasks** - Quickly create new todos with empty field validation
- ✏️ **Inline Edit** - Double-click or click edit button to rename tasks
- 🔄 **Mark Complete** - Toggle task status by clicking checkbox or complete button
- 🗑️ **Delete Tasks** - Remove unwanted tasks with confirmation prompt
- 💾 **Data Persistence** - All data saved in SQLite database

### Advanced Features
- 🔍 **Powerful Search** - Search with fuzzy or exact matching
- 📄 **Pagination** - Navigate through tasks with customizable page size (5/10/20/50)
- 📊 **Real-time Stats** - View total, active, and completed task counts
- 🎯 **Smart Filters** - View all/active/completed tasks
- 🧹 **Batch Operations** - Clear completed or all tasks with warning confirmation

### UI/UX
- 🎨 **Animated Background** - Complex particle effects with floating gradients
- ✨ **Glassmorphism Design** - Semi-transparent cards with blur effects
- 🌈 **Gradient Animations** - Dynamic color transitions and glowing effects
- 📱 **Fully Responsive** - Perfect on mobile, tablet, and desktop
- ⚠️ **Smart Prompts** - Success/failure/warning feedback for all operations
- ♿ **Accessibility** - Screen reader support, WCAG compliant

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern frontend framework
- **Vite** - Fast build tool
- **Axios** - HTTP request library
- **CSS3** - Modern styling

### Backend
- **FastAPI** - High-performance Python web framework
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## 📦 Project Structure

```
work3/
├── backend/                # Backend directory
│   ├── main.py            # FastAPI main application
│   ├── requirements.txt   # Python dependencies
│   ├── todos.db          # SQLite database (auto-generated)
│   └── .gitignore
│
├── frontend/              # Frontend directory
│   ├── src/
│   │   ├── App.jsx       # Main application component
│   │   ├── App.css       # Application styles
│   │   ├── main.jsx      # Entry file
│   │   └── index.css     # Global styles
│   ├── index.html        # HTML template
│   ├── vite.config.js    # Vite configuration
│   ├── package.json      # Frontend dependencies
│   └── .gitignore
│
├── database.sql          # Database table design SQL
└── README.md             # Project documentation
```

## 🚀 Quick Start

### Requirements

- **Node.js** >= 16.0
- **Python** >= 3.8
- **npm** or **yarn**

### 1️⃣ Install Backend Dependencies

```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Start Backend Service

**Method 1: Using Startup Script (Recommended)**
```bash
# In project root directory (work3)
# Windows:
start-backend.bat
# Mac/Linux:
./backend/start.sh
```

**Method 2: Manual Startup**
```bash
# In backend directory, after activating virtual environment
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Backend service will run on `http://localhost:8000`

API Documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 3️⃣ Install Frontend Dependencies

```bash
# Open a new terminal
cd frontend

# Install dependencies
npm install
```

### 4️⃣ Start Frontend Application

**Method 1: Using Startup Script (Recommended)**
```bash
# In project root directory (work3)
# Windows:
start-frontend.bat
# Mac/Linux:
./frontend/start.sh
```

**Method 2: Manual Startup**
```bash
# In frontend directory
npm run dev
```

Frontend application will run on `http://localhost:3000`
> **Note**: Frontend uses Vite dev server, code changes will auto-reload

### 5️⃣ Access Application

Open `http://localhost:3000` in your browser and start using the todo app!

## 📡 API Endpoints

### Get All Todos (with Search & Pagination)
```
GET /api/todos?filter=all|active|completed&search=keyword&search_type=fuzzy|exact&page=1&page_size=10
```
**Parameters:**
- `filter`: all (default), active, completed
- `search`: search keyword (optional)
- `search_type`: fuzzy (default) or exact
- `page`: page number (default: 1)
- `page_size`: items per page (default: 10, 0 = no pagination)

**Response:**
```json
{
  "todos": [...],
  "total": 50,
  "page": 1,
  "page_size": 10,
  "total_pages": 5
}
```

### Get Single Todo
```
GET /api/todos/{id}
```

### Create Todo
```
POST /api/todos
Body: { "text": "Task content" }
```

### Update Todo (Edit Name or Status)
```
PUT /api/todos/{id}
Body: { "text": "New content", "completed": true }
```
*Note: Both fields are optional. You can update just the text or just the status.*

### Delete Todo
```
DELETE /api/todos/{id}
```

### Clear Completed Tasks
```
DELETE /api/todos/clear/completed
```

### Clear All Tasks
```
DELETE /api/todos/clear/all
```

### Get Statistics
```
GET /api/stats
```
**Response:**
```json
{
  "total": 50,
  "active": 30,
  "completed": 20
}
```

## 🗄️ Database Design

```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 UI Design Features

- **Gradient Background** - Smooth purple to pink-purple gradient
- **Glassmorphism** - Semi-transparent cards with blur effect
- **Smooth Animations** - Hover, click, and slide-in animations
- **Responsive Layout** - Adapts to mobile and desktop
- **Visual Feedback** - Instant visual feedback for all interactions

## 📱 Responsive Design

Application perfectly supports:
- 📱 Mobile (320px+)
- 📱 Tablet (640px+)
- 💻 Desktop (1024px+)

## 🔧 Development Commands

### Backend Development
```bash
# Run development server (auto-reload)
uvicorn main:app --reload

# Or run directly
python main.py
```

### Frontend Development
```bash
# Development mode
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📝 Usage Instructions

### Basic Operations
1. **Add Task**: Enter task content in input field, click "Add Task" button
2. **Edit Task**: Double-click task name or click "Edit" button, then save or cancel
3. **Mark Complete**: Click checkbox or "Complete" button
4. **Unmark Complete**: Click checkbox or "Undo" button on completed task
5. **Delete Task**: Click "Delete" button (with confirmation)

### Search & Filter
6. **Search Tasks**: 
   - Enter keyword in search box at the top
   - Toggle between "Fuzzy" (partial match) or "Exact" (exact match)
   - Click "Search" button
   - Click "Clear" to reset search
7. **Filter Tasks**: Click "All", "Active", or "Completed" buttons

### Pagination
8. **Navigate Pages**: Use First/Prev/Next/Last buttons or click page numbers
9. **Change Page Size**: Select 5/10/20/50 items per page from dropdown

### Batch Operations
10. **Clear Completed**: Click "Clear Completed" button at the bottom
11. **Clear All**: Click "Clear All" button (with warning)

## 🔧 Key Technical Fixes

### SQLite Thread Safety Issue
When using SQLite in FastAPI async environment, add `check_same_thread=False` parameter when connecting:
```python
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
```

### Data Type Conversion
SQLite BOOLEAN type is actually stored as integer (0/1), needs to be converted to boolean before returning to frontend:
```python
result['completed'] = bool(result['completed'])
```

### Pydantic V2 Configuration
Use new Pydantic `ConfigDict` instead of old `class Config`:
```python
from pydantic import BaseModel, ConfigDict

class Todo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
```

## 🐛 Common Issues

### 1. Backend Won't Start
- Ensure Python 3.8+ is installed
- Check if port 8000 is occupied: `netstat -ano | findstr "8000"`
- Confirm dependencies are correctly installed: `pip install -r requirements.txt`
- Use `uvicorn main:app` instead of `python main.py`

### 2. Frontend Can't Connect to Backend
- Ensure backend service is running (port 8000)
- Check backend is running on `http://localhost:8000`
- View browser console network error messages
- Confirm Vite proxy configuration is correct

### 3. Data Won't Save
- Ensure backend directory has write permissions
- Check if `todos.db` file is created properly
- View backend console error logs
- Confirm SQLite connection configuration is correct

### 4. No Warning for Empty Input
- Frontend has input validation, empty fields will show `⚠️ Please enter task content!`
- If not working, refresh browser (Vite hot reload)

## 🔐 Security

- ✅ Automatic HTML escaping for input content, prevents XSS attacks
- ✅ API parameter validation using Pydantic models
- ✅ SQL queries use parameterization, prevents SQL injection
- ✅ CORS configuration, restricts cross-origin access

## 📄 License

MIT License

## 👨‍💻 Author

**nikk909**  
📧 Email: yinghua253659@163.com  
🔗 GitHub: [@nikk909](https://github.com/nikk909)

A full-stack todo application developed with modern tech stack

---

**Enjoy using the app!** 🎉

Feel free to submit Issues or PRs if you have any questions.
