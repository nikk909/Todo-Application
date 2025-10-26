# 待办事项应用 - 后端服务文档

## 📋 目录

1. [项目简介](#项目简介)
2. [技术栈](#技术栈)
3. [快速开始](#快速开始)
4. [API 接口文档](#api-接口文档)
5. [数据库设计](#数据库设计)
6. [测试](#测试)
7. [部署](#部署)
8. [故障排查](#故障排查)

---

## 项目简介

基于 FastAPI 构建的高性能待办事项管理后端服务，提供完整的 RESTful API 接口。

### 核心特性

- ✅ **高性能**: FastAPI + Uvicorn ASGI 服务器
- ✅ **自动文档**: Swagger UI / ReDoc 交互式文档
- ✅ **数据验证**: Pydantic 模型自动验证
- ✅ **类型安全**: 完整的类型提示
- ✅ **CORS 支持**: 跨域请求配置
- ✅ **SQLite 数据库**: 轻量级数据持久化

---

## 技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Python | 3.8+ | 编程语言 |
| FastAPI | 0.109.0 | Web 框架 |
| Uvicorn | 0.27.0 | ASGI 服务器 |
| Pydantic | 2.5.3 | 数据验证 |
| SQLite | 3.x | 数据库 |
| Pytest | 7.4.3 | 测试框架 |

---

## 快速开始

### 方式 1: 使用启动脚本（推荐）

#### Windows
```bash
start.bat
```

#### Linux/Mac
```bash
chmod +x start.sh
./start.sh
```

### 方式 2: 手动启动

#### 1. 创建虚拟环境
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 2. 安装依赖
```bash
pip install -r requirements.txt
```

#### 3. 初始化数据库（可选）
```bash
# 空数据库
python init_db.py init

# 包含示例数据
python init_db.py init-sample
```

#### 4. 启动服务
```bash
python main.py
```

### 访问服务

- **API 根路径**: http://localhost:8000
- **Swagger UI 文档**: http://localhost:8000/docs
- **ReDoc 文档**: http://localhost:8000/redoc

---

## API 接口文档

### 基础信息

- **Base URL**: `http://localhost:8000`
- **Content-Type**: `application/json`
- **字符编码**: `UTF-8`

### 接口列表

#### 1. 健康检查

```http
GET /
```

**响应示例**:
```json
{
    "message": "待办事项 API 服务正常运行",
    "version": "1.0.0"
}
```

---

#### 2. 获取任务列表

```http
GET /api/todos?filter={all|active|completed}
```

**查询参数**:
| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| filter | string | 否 | all | all(全部), active(未完成), completed(已完成) |

**响应示例**:
```json
[
    {
        "id": 1,
        "text": "完成项目文档",
        "completed": false,
        "created_at": "2025-10-26T10:30:00",
        "updated_at": "2025-10-26T10:30:00"
    }
]
```

---

#### 3. 获取单个任务

```http
GET /api/todos/{id}
```

**响应示例**:
```json
{
    "id": 1,
    "text": "完成项目文档",
    "completed": false,
    "created_at": "2025-10-26T10:30:00",
    "updated_at": "2025-10-26T10:30:00"
}
```

**错误响应**:
```json
{
    "detail": "待办事项不存在"
}
```

---

#### 4. 创建新任务

```http
POST /api/todos
Content-Type: application/json

{
    "text": "新任务内容"
}
```

**请求体**:
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 是 | 任务内容 |

**响应示例**: (状态码: 201)
```json
{
    "id": 3,
    "text": "新任务内容",
    "completed": false,
    "created_at": "2025-10-26T12:00:00",
    "updated_at": "2025-10-26T12:00:00"
}
```

---

#### 5. 更新任务

```http
PUT /api/todos/{id}
Content-Type: application/json

{
    "text": "更新后的内容",
    "completed": true
}
```

**请求体**:
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 否 | 任务内容 |
| completed | boolean | 否 | 完成状态 |

**响应示例**:
```json
{
    "id": 1,
    "text": "更新后的内容",
    "completed": true,
    "created_at": "2025-10-26T10:30:00",
    "updated_at": "2025-10-26T12:15:00"
}
```

---

#### 6. 删除任务

```http
DELETE /api/todos/{id}
```

**响应示例**:
```json
{
    "message": "删除成功",
    "id": 1
}
```

---

#### 7. 清除已完成任务

```http
DELETE /api/todos/clear/completed
```

**响应示例**:
```json
{
    "message": "已清除所有已完成任务",
    "count": 5
}
```

---

#### 8. 清空所有任务

```http
DELETE /api/todos/clear/all
```

**响应示例**:
```json
{
    "message": "已清空所有任务",
    "count": 10
}
```

---

#### 9. 获取统计信息

```http
GET /api/stats
```

**响应示例**:
```json
{
    "total": 10,
    "completed": 4,
    "active": 6
}
```

---

### HTTP 状态码

| 状态码 | 说明 | 场景 |
|--------|------|------|
| 200 | 成功 | GET, PUT, DELETE 成功 |
| 201 | 已创建 | POST 创建成功 |
| 400 | 请求错误 | 参数验证失败 |
| 404 | 未找到 | 资源不存在 |
| 422 | 无法处理 | Pydantic 验证错误 |
| 500 | 服务器错误 | 内部异常 |

---

## 数据库设计

### todos 表

| 字段 | 类型 | 约束 | 默认值 | 说明 |
|------|------|------|--------|------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | - | 主键 |
| text | TEXT | NOT NULL | - | 任务内容 |
| completed | BOOLEAN | NOT NULL | 0 | 完成状态 |
| created_at | TIMESTAMP | - | CURRENT_TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | - | CURRENT_TIMESTAMP | 更新时间 |

### 索引

```sql
CREATE INDEX idx_todos_completed ON todos(completed);
CREATE INDEX idx_todos_created_at ON todos(created_at DESC);
```

---

## 测试

### 运行单元测试

```bash
# 安装测试依赖
pip install -r requirements-test.txt

# 运行所有测试
pytest test_api.py -v

# 运行特定测试类
pytest test_api.py::TestTodosCRUD -v

# 查看测试覆盖率
pytest test_api.py --cov=main --cov-report=html
```

### 使用 Postman 测试

1. 导入 `postman_collection.json`
2. 确保服务运行在 `http://localhost:8000`
3. 按顺序执行请求

### 使用 curl 测试

```bash
# 获取所有任务
curl http://localhost:8000/api/todos

# 创建任务
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"text":"测试任务"}'

# 更新任务
curl -X PUT http://localhost:8000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'

# 删除任务
curl -X DELETE http://localhost:8000/api/todos/1
```

---

## 数据库管理

### 使用 init_db.py 工具

```bash
# 初始化空数据库
python init_db.py init

# 初始化并添加示例数据
python init_db.py init-sample

# 查看统计信息
python init_db.py stats

# 导出数据
python init_db.py export

# 重置数据库
python init_db.py reset
```

### 交互式管理

```bash
python init_db.py
```

然后按照菜单提示操作。

---

## 部署

### 开发环境

```bash
python main.py
```

服务运行在 `http://localhost:8000`，启用自动重载。

### 生产环境

#### 使用 Gunicorn

```bash
pip install gunicorn

gunicorn main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --access-logfile - \
    --error-logfile -
```

#### 使用 Docker

创建 `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

构建并运行:
```bash
docker build -t todo-backend .
docker run -p 8000:8000 -v $(pwd):/app todo-backend
```

---

## 故障排查

### 问题 1: 端口被占用

**错误信息**: `Address already in use`

**解决方案**:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <进程ID> /F

# Linux/Mac
lsof -i :8000
kill -9 <进程ID>

# 或修改端口
uvicorn main:app --port 8001
```

### 问题 2: 数据库锁定

**错误信息**: `database is locked`

**解决方案**:
- 确保没有其他进程访问数据库
- 重启应用
- 使用 `init_db.py reset` 重置数据库

### 问题 3: 导入错误

**错误信息**: `ModuleNotFoundError`

**解决方案**:
```bash
# 确保虚拟环境已激活
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 重新安装依赖
pip install -r requirements.txt
```

### 问题 4: CORS 错误

**错误信息**: `CORS policy: No 'Access-Control-Allow-Origin'`

**解决方案**:
在 `main.py` 中添加前端地址到 `allow_origins`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://your-frontend-url"],
    ...
)
```

---

## 项目结构

```
backend/
├── main.py                      # FastAPI 主应用
├── test_api.py                  # API 测试
├── init_db.py                   # 数据库管理工具
├── requirements.txt             # 生产依赖
├── requirements-test.txt        # 测试依赖
├── postman_collection.json      # Postman 测试集合
├── start.sh                     # Linux/Mac 启动脚本
├── start.bat                    # Windows 启动脚本
├── README_BACKEND.md            # 本文档
├── .gitignore                   # Git 忽略配置
└── todos.db                     # SQLite 数据库（运行时生成）
```

---

## 开发指南

### 添加新接口

1. 在 `main.py` 中定义路由函数
2. 使用 Pydantic 模型验证数据
3. 添加对应的测试用例
4. 更新 API 文档

示例:
```python
@app.get("/api/todos/{id}/history")
async def get_todo_history(id: int, conn = Depends(get_db)):
    """获取任务历史记录"""
    # 实现逻辑
    return {"history": []}
```

### 代码规范

- 遵循 PEP 8 编码规范
- 使用类型提示
- 添加文档字符串
- 编写单元测试

---

## 性能优化

### 数据库优化

- 使用索引加速查询
- 避免 N+1 查询问题
- 合理使用 LIMIT 和 OFFSET

### API 优化

- 使用异步路由 (`async def`)
- 启用响应压缩
- 实现缓存机制（如需要）

---

## 安全建议

- ✅ 使用参数化查询防止 SQL 注入
- ✅ 配置 CORS 限制来源
- ✅ 启用 HTTPS（生产环境）
- ✅ 添加请求速率限制（可选）
- ✅ 实现用户认证（如需要）

---

## 相关资源

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Pydantic 文档](https://docs.pydantic.dev/)
- [SQLite 文档](https://www.sqlite.org/docs.html)
- [Uvicorn 文档](https://www.uvicorn.org/)

---

## 许可证

MIT License

---

## 联系方式

如有问题，请查看主项目 README 或提交 Issue。

---

**文档版本**: 1.0.0  
**最后更新**: 2025-10-26

