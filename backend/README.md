# Backend API Service

FastAPI Todo Application Backend Service.

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Start Service

```bash
python main.py
```

Service will run on `http://localhost:8000`

## API Documentation

After starting the service, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Main Features

- ✅ RESTful API design
- ✅ Automatic data validation (Pydantic)
- ✅ SQLite database persistence
- ✅ CORS cross-origin support
- ✅ Automatic interactive documentation

## Database

The application will automatically create a `todos.db` SQLite database file on startup.
