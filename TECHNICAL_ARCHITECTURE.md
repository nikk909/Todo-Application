# 待办事项应用 - 技术架构文档

## 📋 文档信息

| 项目 | 信息 |
|------|------|
| **项目名称** | 待办事项应用 (Todo Application) |
| **版本** | 1.0.0 |
| **文档类型** | 技术架构文档 |
| **创建日期** | 2025-10-26 |
| **最后更新** | 2025-10-26 |

---

## 📑 目录

1. [系统概述](#1-系统概述)
2. [技术栈](#2-技术栈)
3. [系统架构](#3-系统架构)
4. [数据库设计](#4-数据库设计)
5. [API 接口设计](#5-api-接口设计)
6. [前端架构](#6-前端架构)
7. [后端架构](#7-后端架构)
8. [部署方案](#8-部署方案)
9. [安全设计](#9-安全设计)
10. [性能优化](#10-性能优化)

---

## 1. 系统概述

### 1.1 项目背景

开发一个现代化的待办事项管理应用，帮助用户高效管理日常任务。应用采用前后端分离架构，提供直观的用户界面和强大的后端支持。

### 1.2 核心功能

- **任务管理**: 创建、查看、更新、删除任务
- **状态管理**: 标记任务完成/未完成
- **任务筛选**: 按完成状态筛选任务
- **批量操作**: 批量清除已完成或所有任务
- **数据持久化**: 所有数据存储在数据库中

### 1.3 技术目标

- ✅ 高性能：快速响应用户操作
- ✅ 可维护：代码结构清晰，易于扩展
- ✅ 可扩展：模块化设计，便于添加新功能
- ✅ 安全性：防止常见 Web 安全漏洞
- ✅ 用户体验：流畅的动画和交互

---

## 2. 技术栈

### 2.1 前端技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **React** | 18.2.0 | UI 框架 |
| **Vite** | 5.0.11 | 构建工具和开发服务器 |
| **Axios** | 1.6.5 | HTTP 客户端 |
| **CSS3** | - | 样式设计 |
| **JavaScript (ES6+)** | - | 编程语言 |

**前端技术选型理由：**
- **React**: 组件化开发，虚拟 DOM 高性能，生态完善
- **Vite**: 快速的冷启动，HMR 热更新，开箱即用
- **Axios**: 基于 Promise，支持拦截器，易于使用

### 2.2 后端技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **FastAPI** | 0.109.0 | Web 框架 |
| **Uvicorn** | 0.27.0 | ASGI 服务器 |
| **Pydantic** | 2.5.3 | 数据验证 |
| **SQLite** | 3.x | 关系型数据库 |
| **Python** | 3.8+ | 编程语言 |

**后端技术选型理由：**
- **FastAPI**: 高性能，自动生成文档，类型提示，异步支持
- **SQLite**: 轻量级，无需额外配置，适合小型应用
- **Pydantic**: 数据验证，类型安全，IDE 友好

### 2.3 开发工具

- **IDE**: VS Code / PyCharm / Cursor
- **版本控制**: Git
- **包管理**: npm (前端) / pip (后端)
- **API 测试**: Postman / Swagger UI

---

## 3. 系统架构

### 3.1 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                        用户浏览器                              │
└─────────────────┬───────────────────────────────────────────┘
                  │ HTTP/HTTPS
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                     前端应用 (React)                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  UI 组件层                                             │  │
│  │  - App.jsx (主组件)                                    │  │
│  │  - 任务列表、表单、筛选器                                │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  状态管理层                                             │  │
│  │  - React Hooks (useState, useEffect)                  │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  HTTP 客户端层                                          │  │
│  │  - Axios (API 请求)                                    │  │
│  └──────────────────┬───────────────────────────────────┘  │
└────────────────────┼────────────────────────────────────────┘
                     │ RESTful API
                     │ JSON
┌────────────────────▼────────────────────────────────────────┐
│                    后端服务 (FastAPI)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  API 路由层                                             │  │
│  │  - 任务 CRUD 接口                                       │  │
│  │  - 筛选、批量操作接口                                    │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  业务逻辑层                                             │  │
│  │  - 数据验证 (Pydantic)                                 │  │
│  │  - 业务规则处理                                         │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  数据访问层                                             │  │
│  │  - SQLite 连接管理                                     │  │
│  │  - SQL 查询执行                                        │  │
│  └──────────────────┬───────────────────────────────────┘  │
└────────────────────┼────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   SQLite 数据库                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  todos 表                                              │  │
│  │  - 任务数据存储                                         │  │
│  │  - 索引优化                                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 目录结构

```
work3/
├── backend/                      # 后端应用
│   ├── main.py                  # FastAPI 主应用入口
│   ├── requirements.txt         # Python 依赖
│   ├── todos.db                 # SQLite 数据库文件（自动生成）
│   ├── README.md                # 后端文档
│   └── .gitignore
│
├── frontend/                     # 前端应用
│   ├── src/                     # 源代码目录
│   │   ├── main.jsx            # React 应用入口
│   │   ├── App.jsx             # 主应用组件
│   │   ├── App.css             # 应用样式
│   │   └── index.css           # 全局样式
│   ├── index.html              # HTML 模板
│   ├── vite.config.js          # Vite 配置
│   ├── package.json            # NPM 依赖
│   ├── README.md               # 前端文档
│   └── .gitignore
│
├── database.sql                 # 数据库初始化脚本
├── README.md                    # 项目主文档
└── TECHNICAL_ARCHITECTURE.md    # 本文档
```

### 3.3 通信流程

```
用户操作
   │
   ├─→ 添加任务
   │     ├─→ 前端: 提交表单
   │     ├─→ 发送: POST /api/todos
   │     ├─→ 后端: 验证数据 → 插入数据库
   │     └─→ 返回: 新任务对象
   │
   ├─→ 查看任务
   │     ├─→ 前端: 组件挂载
   │     ├─→ 发送: GET /api/todos?filter=all
   │     ├─→ 后端: 查询数据库
   │     └─→ 返回: 任务列表
   │
   ├─→ 标记完成
   │     ├─→ 前端: 点击复选框
   │     ├─→ 发送: PUT /api/todos/{id}
   │     ├─→ 后端: 更新数据库
   │     └─→ 返回: 更新后的任务
   │
   └─→ 删除任务
         ├─→ 前端: 点击删除按钮
         ├─→ 发送: DELETE /api/todos/{id}
         ├─→ 后端: 从数据库删除
         └─→ 返回: 成功消息
```

---

## 4. 数据库设计

### 4.1 数据库选型

**选择 SQLite 的原因：**
- ✅ 轻量级，无需独立服务器
- ✅ 零配置，开箱即用
- ✅ 适合小型应用和原型开发
- ✅ 支持标准 SQL
- ✅ 跨平台，易于部署

### 4.2 ER 图

```
┌─────────────────────────────────────────┐
│              todos 表                    │
├─────────────────────────────────────────┤
│ PK  id           INTEGER                │
│     text         TEXT                   │
│     completed    BOOLEAN                │
│     created_at   TIMESTAMP              │
│     updated_at   TIMESTAMP              │
└─────────────────────────────────────────┘
```

### 4.3 表设计

#### 4.3.1 todos 表

**表名**: `todos`

**功能**: 存储所有待办事项数据

**字段说明**:

| 字段名 | 类型 | 约束 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | - | 任务唯一标识符 |
| `text` | TEXT | NOT NULL | - | 任务内容描述 |
| `completed` | BOOLEAN | NOT NULL | 0 (false) | 任务完成状态 |
| `created_at` | TIMESTAMP | - | CURRENT_TIMESTAMP | 任务创建时间 |
| `updated_at` | TIMESTAMP | - | CURRENT_TIMESTAMP | 任务最后更新时间 |

**索引设计**:

| 索引名 | 类型 | 字段 | 说明 |
|--------|------|------|------|
| `idx_todos_completed` | 普通索引 | `completed` | 优化按完成状态筛选 |
| `idx_todos_created_at` | 普通索引 | `created_at DESC` | 优化按创建时间排序 |

### 4.4 SQL DDL 语句

```sql
-- ============================================
-- 待办事项应用数据库初始化脚本
-- 数据库类型: SQLite 3.x
-- ============================================

-- 创建待办事项表
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引以提高查询性能
-- 按完成状态筛选的索引
CREATE INDEX IF NOT EXISTS idx_todos_completed 
    ON todos(completed);

-- 按创建时间排序的索引（降序）
CREATE INDEX IF NOT EXISTS idx_todos_created_at 
    ON todos(created_at DESC);

-- ============================================
-- 示例数据（可选）
-- ============================================

INSERT INTO todos (text, completed) VALUES
    ('完成项目文档', 0),
    ('学习 React 新特性', 0),
    ('代码审查', 1),
    ('参加团队会议', 0);
```

### 4.5 常用 SQL 查询

#### 4.5.1 查询所有任务

```sql
-- 查询所有任务（按创建时间倒序）
SELECT * FROM todos 
ORDER BY created_at DESC;
```

#### 4.5.2 查询未完成任务

```sql
-- 查询所有未完成的任务
SELECT * FROM todos 
WHERE completed = 0 
ORDER BY created_at DESC;
```

#### 4.5.3 查询已完成任务

```sql
-- 查询所有已完成的任务
SELECT * FROM todos 
WHERE completed = 1 
ORDER BY created_at DESC;
```

#### 4.5.4 插入新任务

```sql
-- 插入一条新任务
INSERT INTO todos (text, completed, created_at, updated_at) 
VALUES ('新任务内容', 0, datetime('now'), datetime('now'));
```

#### 4.5.5 更新任务状态

```sql
-- 标记任务为已完成
UPDATE todos 
SET completed = 1, updated_at = datetime('now') 
WHERE id = ?;
```

#### 4.5.6 删除任务

```sql
-- 删除指定任务
DELETE FROM todos WHERE id = ?;
```

#### 4.5.7 批量删除已完成任务

```sql
-- 删除所有已完成的任务
DELETE FROM todos WHERE completed = 1;
```

#### 4.5.8 清空所有任务

```sql
-- 删除所有任务
DELETE FROM todos;
```

#### 4.5.9 统计查询

```sql
-- 统计任务数量
SELECT 
    COUNT(*) as total,
    SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END) as completed_count,
    SUM(CASE WHEN completed = 0 THEN 1 ELSE 0 END) as active_count
FROM todos;
```

---

## 5. API 接口设计

### 5.1 API 设计原则

- ✅ RESTful 风格
- ✅ 统一的响应格式
- ✅ 清晰的错误信息
- ✅ 版本化管理
- ✅ 完善的文档

### 5.2 基础配置

**Base URL**: `http://localhost:8000`

**API 前缀**: `/api`

**Content-Type**: `application/json`

**字符编码**: `UTF-8`

### 5.3 API 接口列表

#### 5.3.1 健康检查

**接口描述**: 检查 API 服务是否正常运行

**请求**:
```http
GET /
```

**响应**:
```json
{
    "message": "待办事项 API 服务正常运行",
    "version": "1.0.0"
}
```

**状态码**: `200 OK`

---

#### 5.3.2 获取任务列表

**接口描述**: 获取所有待办事项，支持按状态筛选

**请求**:
```http
GET /api/todos?filter={all|active|completed}
```

**请求参数**:

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `filter` | string | 否 | all | 筛选条件：all(全部)、active(未完成)、completed(已完成) |

**响应示例**:
```json
[
    {
        "id": 1,
        "text": "完成项目文档",
        "completed": false,
        "created_at": "2025-10-26T10:30:00",
        "updated_at": "2025-10-26T10:30:00"
    },
    {
        "id": 2,
        "text": "学习 React",
        "completed": true,
        "created_at": "2025-10-26T09:15:00",
        "updated_at": "2025-10-26T11:20:00"
    }
]
```

**状态码**: `200 OK`

---

#### 5.3.3 获取单个任务

**接口描述**: 根据任务 ID 获取任务详情

**请求**:
```http
GET /api/todos/{id}
```

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `id` | integer | 是 | 任务 ID |

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

**状态码**: `200 OK`

**错误响应**:
```json
{
    "detail": "待办事项不存在"
}
```
**状态码**: `404 Not Found`

---

#### 5.3.4 创建新任务

**接口描述**: 创建一条新的待办事项

**请求**:
```http
POST /api/todos
Content-Type: application/json

{
    "text": "新任务内容"
}
```

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `text` | string | 是 | 任务内容，不能为空 |

**响应示例**:
```json
{
    "id": 3,
    "text": "新任务内容",
    "completed": false,
    "created_at": "2025-10-26T12:00:00",
    "updated_at": "2025-10-26T12:00:00"
}
```

**状态码**: `201 Created`

**错误响应**:
```json
{
    "detail": [
        {
            "loc": ["body", "text"],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```
**状态码**: `422 Unprocessable Entity`

---

#### 5.3.5 更新任务

**接口描述**: 更新任务的内容或完成状态

**请求**:
```http
PUT /api/todos/{id}
Content-Type: application/json

{
    "text": "更新后的任务内容",
    "completed": true
}
```

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `id` | integer | 是 | 任务 ID |

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `text` | string | 否 | 任务内容 |
| `completed` | boolean | 否 | 完成状态 |

**响应示例**:
```json
{
    "id": 1,
    "text": "更新后的任务内容",
    "completed": true,
    "created_at": "2025-10-26T10:30:00",
    "updated_at": "2025-10-26T12:15:00"
}
```

**状态码**: `200 OK`

**错误响应**:
```json
{
    "detail": "待办事项不存在"
}
```
**状态码**: `404 Not Found`

---

#### 5.3.6 删除任务

**接口描述**: 删除指定的待办事项

**请求**:
```http
DELETE /api/todos/{id}
```

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `id` | integer | 是 | 任务 ID |

**响应示例**:
```json
{
    "message": "删除成功",
    "id": 1
}
```

**状态码**: `200 OK`

**错误响应**:
```json
{
    "detail": "待办事项不存在"
}
```
**状态码**: `404 Not Found`

---

#### 5.3.7 清除已完成任务

**接口描述**: 批量删除所有已完成的任务

**请求**:
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

**状态码**: `200 OK`

---

#### 5.3.8 清空所有任务

**接口描述**: 批量删除所有任务

**请求**:
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

**状态码**: `200 OK`

---

#### 5.3.9 获取统计信息

**接口描述**: 获取任务的统计数据

**请求**:
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

**状态码**: `200 OK`

---

### 5.4 API 状态码说明

| 状态码 | 说明 | 使用场景 |
|--------|------|---------|
| `200 OK` | 请求成功 | GET、PUT、DELETE 成功 |
| `201 Created` | 资源创建成功 | POST 创建成功 |
| `400 Bad Request` | 请求参数错误 | 参数验证失败 |
| `404 Not Found` | 资源不存在 | 查询或操作不存在的资源 |
| `422 Unprocessable Entity` | 数据验证失败 | Pydantic 验证错误 |
| `500 Internal Server Error` | 服务器内部错误 | 服务器异常 |

### 5.5 错误响应格式

```json
{
    "detail": "错误详细信息"
}
```

或者（Pydantic 验证错误）:
```json
{
    "detail": [
        {
            "loc": ["body", "field_name"],
            "msg": "错误消息",
            "type": "错误类型"
        }
    ]
}
```

### 5.6 API 测试示例

#### 使用 curl 测试

```bash
# 1. 获取所有任务
curl -X GET http://localhost:8000/api/todos

# 2. 创建新任务
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"text":"测试任务"}'

# 3. 更新任务（标记为完成）
curl -X PUT http://localhost:8000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'

# 4. 删除任务
curl -X DELETE http://localhost:8000/api/todos/1

# 5. 清除已完成任务
curl -X DELETE http://localhost:8000/api/todos/clear/completed
```

#### 使用 JavaScript (Axios) 测试

```javascript
// 获取所有任务
const getTodos = async () => {
    const response = await axios.get('/api/todos');
    console.log(response.data);
};

// 创建新任务
const createTodo = async (text) => {
    const response = await axios.post('/api/todos', { text });
    console.log(response.data);
};

// 更新任务
const updateTodo = async (id, completed) => {
    const response = await axios.put(`/api/todos/${id}`, { completed });
    console.log(response.data);
};

// 删除任务
const deleteTodo = async (id) => {
    const response = await axios.delete(`/api/todos/${id}`);
    console.log(response.data);
};
```

---

## 6. 前端架构

### 6.1 技术栈

- **React 18**: 函数式组件 + Hooks
- **Vite**: 快速开发和构建
- **Axios**: HTTP 请求库
- **CSS3**: 样式设计

### 6.2 组件结构

```
App.jsx (主组件)
├── Header (标题)
│   └── <h1>我的待办事项</h1>
│
├── AddSection (添加任务区域)
│   └── <form>
│       ├── <input> (输入框)
│       └── <button> (添加按钮)
│
├── ControlSection (控制区域)
│   ├── TaskStats (任务统计)
│   │   └── 共 X 项任务
│   └── FilterButtons (筛选按钮组)
│       ├── 全部
│       ├── 未完成
│       └── 已完成
│
├── ListSection (任务列表区域)
│   ├── TodoList
│   │   └── TodoItem[] (任务项)
│   │       ├── Checkbox (复选框)
│   │       ├── Text (任务内容)
│   │       └── Actions (操作按钮)
│   │           ├── CompleteButton
│   │           └── DeleteButton
│   └── EmptyState (空状态)
│
└── ActionSection (底部操作区域)
    ├── ClearCompletedButton
    └── ClearAllButton
```

### 6.3 状态管理

```javascript
// 应用状态
const [todos, setTodos] = useState([])           // 任务列表
const [inputValue, setInputValue] = useState('') // 输入框值
const [currentFilter, setCurrentFilter] = useState('all') // 当前筛选
const [loading, setLoading] = useState(false)    // 加载状态
```

### 6.4 核心逻辑

#### 数据获取
```javascript
useEffect(() => {
    fetchTodos(currentFilter);
}, [currentFilter]);
```

#### API 调用封装
```javascript
const API_BASE = '/api';

// 获取任务
const fetchTodos = async (filter) => {
    const response = await axios.get(`${API_BASE}/todos`, {
        params: filter !== 'all' ? { filter } : {}
    });
    setTodos(response.data);
};

// 添加任务
const handleAddTodo = async (text) => {
    await axios.post(`${API_BASE}/todos`, { text });
    fetchTodos(currentFilter);
};

// 切换完成状态
const toggleTodo = async (id, completed) => {
    await axios.put(`${API_BASE}/todos/${id}`, {
        completed: !completed
    });
    fetchTodos(currentFilter);
};

// 删除任务
const deleteTodo = async (id) => {
    await axios.delete(`${API_BASE}/todos/${id}`);
    fetchTodos(currentFilter);
};
```

### 6.5 样式设计

**设计原则**:
- 渐变紫色背景（#667eea → #764ba2）
- 白色玻璃拟态卡片
- 圆角设计（8-12px）
- 平滑动画效果
- 响应式布局

**关键 CSS 变量**:
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --success-color: #48bb78;
    --danger-color: #fc8181;
    --text-color: #2d3748;
    --border-radius: 12px;
}
```

---

## 7. 后端架构

### 7.1 技术栈

- **FastAPI**: Web 框架
- **Uvicorn**: ASGI 服务器
- **Pydantic**: 数据验证
- **SQLite**: 数据库

### 7.2 项目结构

```python
main.py
├── 导入依赖
├── FastAPI 应用初始化
├── CORS 中间件配置
├── 数据库配置
├── Pydantic 模型定义
│   ├── TodoCreate (创建任务)
│   ├── TodoUpdate (更新任务)
│   └── Todo (任务响应)
├── 数据库连接管理
│   ├── get_db() (依赖注入)
│   └── init_db() (初始化)
└── API 路由
    ├── GET / (健康检查)
    ├── GET /api/todos (获取列表)
    ├── GET /api/todos/{id} (获取单个)
    ├── POST /api/todos (创建)
    ├── PUT /api/todos/{id} (更新)
    ├── DELETE /api/todos/{id} (删除)
    ├── DELETE /api/todos/clear/completed
    ├── DELETE /api/todos/clear/all
    └── GET /api/stats (统计)
```

### 7.3 数据模型

```python
# 创建任务请求模型
class TodoCreate(BaseModel):
    text: str

# 更新任务请求模型
class TodoUpdate(BaseModel):
    text: Optional[str] = None
    completed: Optional[bool] = None

# 任务响应模型
class Todo(BaseModel):
    id: int
    text: str
    completed: bool
    created_at: str
    updated_at: str
```

### 7.4 数据库连接管理

```python
def get_db():
    """数据库连接依赖注入"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
```

### 7.5 启动配置

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0",  # 监听所有网络接口
        port=8000,        # 端口号
        reload=True       # 开发模式自动重载
    )
```

---

## 8. 部署方案

### 8.1 开发环境部署

#### 后端部署
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 前端部署
```bash
cd frontend
npm install
npm run dev
```

### 8.2 生产环境部署

#### 后端生产部署
```bash
# 使用 Gunicorn + Uvicorn Workers
pip install gunicorn
gunicorn main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
```

#### 前端生产部署
```bash
# 构建生产版本
npm run build

# 使用 Nginx 或其他静态服务器托管 dist/ 目录
```

### 8.3 Docker 部署（可选）

#### 后端 Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 前端 Dockerfile
```dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### Docker Compose
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
  
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

---

## 9. 安全设计

### 9.1 安全措施

#### 9.1.1 XSS 防护
- React 自动转义 HTML
- 不使用 `dangerouslySetInnerHTML`

#### 9.1.2 SQL 注入防护
```python
# ✅ 正确：使用参数化查询
cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))

# ❌ 错误：拼接 SQL（易受 SQL 注入攻击）
cursor.execute(f"SELECT * FROM todos WHERE id = {todo_id}")
```

#### 9.1.3 CORS 配置
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 限制来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 9.1.4 输入验证
- 使用 Pydantic 自动验证
- 后端二次验证
- 前端表单验证

### 9.2 安全检查清单

- ✅ 参数化 SQL 查询
- ✅ CORS 正确配置
- ✅ 输入数据验证
- ✅ XSS 防护
- ✅ HTTPS（生产环境）
- ✅ 敏感数据加密（如需要）

---

## 10. 性能优化

### 10.1 数据库优化

#### 索引优化
```sql
-- 为常用查询字段创建索引
CREATE INDEX idx_todos_completed ON todos(completed);
CREATE INDEX idx_todos_created_at ON todos(created_at DESC);
```

#### 查询优化
- 使用 WHERE 子句减少返回数据
- 避免 SELECT *，只查询需要的字段
- 合理使用 LIMIT 和 OFFSET

### 10.2 前端优化

#### React 优化
- 使用 `React.memo` 避免不必要的重渲染
- 合理使用 `useCallback` 和 `useMemo`
- 懒加载组件（如需要）

#### 网络优化
- API 请求合并
- 使用 Loading 状态提升用户体验
- 错误重试机制

### 10.3 后端优化

#### FastAPI 优化
- 使用异步路由（`async def`）
- 连接池管理
- 响应数据压缩

#### 缓存策略
- 数据库查询结果缓存（可选）
- 静态资源缓存

---

## 11. 监控与日志

### 11.1 日志记录

#### 后端日志
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("应用启动成功")
```

#### 前端日志
```javascript
// 开发环境
if (process.env.NODE_ENV === 'development') {
    console.log('API Response:', response.data);
}

// 生产环境使用专业日志服务
```

### 11.2 性能监控

- API 响应时间
- 数据库查询时间
- 前端页面加载时间
- 错误率统计

---

## 12. 测试策略

### 12.1 单元测试

#### 后端测试（pytest）
```python
def test_create_todo():
    response = client.post("/api/todos", json={"text": "测试任务"})
    assert response.status_code == 201
    assert response.json()["text"] == "测试任务"
```

#### 前端测试（Jest + React Testing Library）
```javascript
test('renders todo item', () => {
    render(<TodoItem text="测试任务" />);
    expect(screen.getByText('测试任务')).toBeInTheDocument();
});
```

### 12.2 集成测试

- API 端到端测试
- 前后端联调测试
- 数据库操作测试

### 12.3 手动测试清单

- [ ] 添加任务功能
- [ ] 标记完成功能
- [ ] 删除任务功能
- [ ] 筛选功能
- [ ] 批量操作功能
- [ ] 响应式设计
- [ ] 错误处理

---

## 13. 附录

### 13.1 开发规范

#### 代码规范
- **Python**: PEP 8
- **JavaScript**: ESLint + Prettier
- **Git**: Conventional Commits

#### 命名规范
- 变量：小驼峰 `camelCase`
- 常量：大写蛇形 `UPPER_SNAKE_CASE`
- 组件：大驼峰 `PascalCase`
- 文件：小写短横线 `kebab-case.js`

### 13.2 相关资源

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [React 官方文档](https://react.dev/)
- [SQLite 文档](https://www.sqlite.org/docs.html)
- [Vite 文档](https://vitejs.dev/)

### 13.3 版本历史

| 版本 | 日期 | 变更说明 |
|------|------|---------|
| 1.0.0 | 2025-10-26 | 初始版本 |

---

## 📞 联系方式

如有技术问题，请参考项目 README 或提交 Issue。

---

**文档结束** 📄

