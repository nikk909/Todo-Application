# Todo App - Quick Start Guide

## ✅ Project Successfully Started!

### 📡 Service Status

| Service | Port | Access URL | Status |
|---------|------|------------|--------|
| **Backend API** | 8000 | http://localhost:8000 | ✅ Running |
| **Frontend UI** | 3000 | http://localhost:3000 | ✅ Running |
| **API Docs** | 8000 | http://localhost:8000/docs | ✅ Available |

---

## 🚀 Startup Methods

### Method 1: Using Startup Scripts (Recommended)

#### Windows Users:
```bash
# Backend (new window)
start-backend.bat

# Frontend (new window)
start-frontend.bat
```

#### Linux/Mac Users:
```bash
# Backend
chmod +x backend/start.sh
./backend/start.sh

# Frontend
cd frontend
npm run dev
```

### Method 2: Manual Startup

#### Start Backend:
```bash
cd backend
.\venv\Scripts\activate.ps1
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### Start Frontend:
```bash
cd frontend
npm run dev
```

---

## 🌐 Access Application

### Frontend Interface
Open browser and visit: **http://localhost:3000**

### API Documentation (Swagger UI)
Open browser and visit: **http://localhost:8000/docs**

- Visual API interface documentation
- Support online testing for all API endpoints
- View request/response formats

---

## 🧪 Test API

### 1. Health Check
```bash
curl http://localhost:8000/
```

### 2. Get All Todos
```bash
curl http://localhost:8000/api/todos
```

### 3. Create New Task
```bash
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"Test Task\"}"
```

### 4. View Statistics
```bash
curl http://localhost:8000/api/stats
```

---

## 🛠 Common Commands

### Check Service Status
```powershell
# Check port usage
netstat -ano | Select-String ":8000|:3000"

# View processes
Get-Process | Where-Object {$_.ProcessName -like '*python*' -or $_.ProcessName -like '*node*'}
```

### Stop Services
```powershell
# Close the corresponding terminal window, or use Ctrl+C
```

### Restart Services
1. Stop the currently running service (Ctrl+C or close window)
2. Re-run the startup script

---

## 📚 Features

### ✨ Frontend Features
- ✅ **Add New Task** - With empty field validation, shows warning when input is empty
- ✅ **Mark Task Complete/Incomplete** - Click checkbox or complete button
- ✅ **Delete Single Task** - With confirmation dialog to prevent accidental deletion
- ✅ **Filter by Status** - All/Incomplete/Completed, real-time switching
- ✅ **Clear All Completed Tasks** - With warning confirmation
- ✅ **Clear All Tasks** - With strict warning confirmation
- ✅ **Real-time Statistics** - Shows total, incomplete, and completed counts
- ✅ **Operation Feedback** - All operations have success/failure/warning prompts
- ✅ **Responsive Design** - Supports mobile, smooth animations
- ♿ **Accessibility Optimization** - Supports screen readers

### 🔌 API Endpoints
- `GET /` - Health check
- `GET /api/todos` - Get todo list (supports filtering)
- `GET /api/todos/{id}` - Get single todo
- `POST /api/todos` - Create new todo
- `PUT /api/todos/{id}` - Update todo
- `DELETE /api/todos/{id}` - Delete todo
- `DELETE /api/todos/clear/completed` - Clear completed
- `DELETE /api/todos/clear/all` - Clear all
- `GET /api/stats` - Get statistics

---

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check virtual environment
cd backend
.\venv\Scripts\activate.ps1

# Reinstall dependencies
pip install --only-binary :all: fastapi uvicorn pydantic python-multipart
```

### Frontend Can't Connect to Backend
1. Confirm backend service is running on port 8000
2. Check `frontend/vite.config.js` proxy configuration
3. View browser console network requests

### Port Already in Use
```powershell
# Find process occupying port
netstat -ano | findstr ":8000"
netstat -ano | findstr ":3000"

# End process (replace PID with actual process ID)
taskkill /PID <ProcessID> /F
```

---

## 📖 More Documentation

- **Technical Architecture**: `TECHNICAL_ARCHITECTURE.md`
- **Project Overview**: `PROJECT_OVERVIEW.md`
- **Backend Documentation**: `backend/README_BACKEND.md`
- **Requirements**: `req.md`

---

## 🎉 Get Started

1. ✅ Backend is running at **http://localhost:8000**
2. ✅ Frontend is running at **http://localhost:3000**
3. 🌐 Open browser and visit **http://localhost:3000** to start using!

---

**Tips**: 
- Backend uses SQLite database, data is saved in `backend/todos.db`
- Frontend supports hot reload, automatically refreshes after code changes
- API Documentation (Swagger UI) provides complete interface testing functionality


