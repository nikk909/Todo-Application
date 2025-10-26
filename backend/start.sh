#!/bin/bash
# 后端启动脚本 (Linux/Mac)

echo "🚀 启动待办事项后端服务..."

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📥 安装依赖..."
pip install -r requirements.txt

# 初始化数据库
if [ ! -f "todos.db" ]; then
    echo "🗄️  初始化数据库..."
    python init_db.py init-sample
fi

# 启动服务
echo "✅ 启动 FastAPI 服务..."
echo "📍 API 地址: http://localhost:8000"
echo "📚 API 文档: http://localhost:8000/docs"
echo ""
python main.py

