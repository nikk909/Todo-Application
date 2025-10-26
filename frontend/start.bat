@echo off
REM 前端启动脚本 (Windows)

echo 🚀 启动待办事项前端应用...

REM 检查 node_modules
if not exist "node_modules\" (
    echo 📦 安装依赖...
    call npm install
)

REM 检查后端服务
echo 🔍 检查后端服务...
curl -s http://localhost:8000/ > nul 2>&1
if errorlevel 1 (
    echo ⚠️  警告: 后端服务未运行！
    echo 请先启动后端服务：
    echo   cd ..\backend
    echo   python main.py
    echo.
    set /p continue="是否继续启动前端？(y/n): "
    if /i not "%continue%"=="y" exit /b 1
)

REM 启动开发服务器
echo ✅ 启动 Vite 开发服务器...
echo 📍 前端地址: http://localhost:3000
echo 📍 后端地址: http://localhost:8000
echo.
npm run dev

