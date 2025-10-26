@echo off
chcp 65001 >nul
echo ====================================
echo 启动待办事项应用 - 后端服务
echo ====================================
cd /d %~dp0\backend

echo.
echo [1/2] 激活虚拟环境...
call venv\Scripts\activate.bat

echo.
echo [2/2] 启动 FastAPI 服务器 (端口 8000)...
echo 访问地址: http://localhost:8000
echo API 文档: http://localhost:8000/docs
echo.
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause

