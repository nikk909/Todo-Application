# 🚀 Quick Start Guide

## Windows Users

### Start Backend
```powershell
# Terminal 1
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Start Frontend
```powershell
# Terminal 2 (open a new one)
cd frontend
npm install
npm run dev
```

## Mac/Linux Users

### Start Backend
```bash
# Terminal 1
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Start Frontend
```bash
# Terminal 2 (open a new one)
cd frontend
npm install
npm run dev
```

## Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Notes

1. Ensure Python 3.8+ and Node.js 16+ are installed
2. Start the backend first, then start the frontend
3. Make sure ports 8000 and 3000 are not occupied
4. The backend will automatically create the `backend/todos.db` database file

## Test API

After the backend starts, you can visit http://localhost:8000/docs to test all API interfaces.
