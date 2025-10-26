#!/bin/bash
# 前端启动脚本 (Linux/Mac)

echo "🚀 启动待办事项前端应用..."

# 检查 node_modules
if [ ! -d "node_modules" ]; then
    echo "📦 安装依赖..."
    npm install
fi

# 检查后端服务
echo "🔍 检查后端服务..."
if ! curl -s http://localhost:8000/ > /dev/null; then
    echo "⚠️  警告: 后端服务未运行！"
    echo "请先启动后端服务："
    echo "  cd ../backend"
    echo "  python main.py"
    echo ""
    read -p "是否继续启动前端？(y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# 启动开发服务器
echo "✅ 启动 Vite 开发服务器..."
echo "📍 前端地址: http://localhost:3000"
echo "📍 后端地址: http://localhost:8000"
echo ""
npm run dev

