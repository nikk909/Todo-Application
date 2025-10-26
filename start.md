# 🚀 快速启动指南

## Windows 用户

### 启动后端
```powershell
# 终端 1
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### 启动前端
```powershell
# 终端 2（新开一个）
cd frontend
npm install
npm run dev
```

## Mac/Linux 用户

### 启动后端
```bash
# 终端 1
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 启动前端
```bash
# 终端 2（新开一个）
cd frontend
npm install
npm run dev
```

## 访问应用

- **前端应用**: http://localhost:3000
- **后端 API**: http://localhost:8000
- **API 文档**: http://localhost:8000/docs

## 注意事项

1. 确保 Python 3.8+ 和 Node.js 16+ 已安装
2. 先启动后端，再启动前端
3. 端口 8000 和 3000 不要被占用
4. 后端会自动创建 `backend/todos.db` 数据库文件

## 测试 API

后端启动后，可以访问 http://localhost:8000/docs 测试所有 API 接口。

