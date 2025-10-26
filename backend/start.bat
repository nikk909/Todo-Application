@echo off
REM 后端启动脚本 (Windows)

echo 🚀 启动待办事项后端服务...

REM 检查虚拟环境
if not exist "venv\" (
    echo 📦 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
echo 🔧 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
echo 📥 安装依赖...
pip install -r requirements.txt

REM 初始化数据库
if not exist "todos.db" (
    echo 🗄️  初始化数据库...
    python init_db.py init-sample
)

REM 启动服务
echo ✅ 启动 FastAPI 服务...
echo 📍 API 地址: http://localhost:8000
echo 📚 API 文档: http://localhost:8000/docs
echo.
python main.py

