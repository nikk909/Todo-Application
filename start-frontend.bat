@echo off
echo ====================================
echo 启动待办事项应用 - 前端服务
echo ====================================
cd /d %~dp0\frontend

echo.
echo 启动 Vite 开发服务器 (端口 3000)...
npm run dev

pause

