# 后端 API 服务

FastAPI 待办事项后端服务。

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python main.py
```

服务将运行在 `http://localhost:8000`

## API 文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 主要功能

- ✅ RESTful API 设计
- ✅ 自动数据验证（Pydantic）
- ✅ SQLite 数据库持久化
- ✅ CORS 跨域支持
- ✅ 自动交互式文档

## 数据库

应用启动时会自动创建 `todos.db` SQLite 数据库文件。

