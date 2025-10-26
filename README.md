# 待办事项应用 📝

一个基于 React + FastAPI + SQLite 的全栈待办事项应用，采用现代化的 UI 设计，提供完整的增删改查功能。

## ✨ 功能特性

- ✅ **添加任务** - 快速创建新的待办事项，带空字段验证
- 🔄 **标记完成** - 点击复选框或完成按钮切换任务状态
- 🗑️ **删除任务** - 删除不需要的任务，带确认提示
- 🔍 **智能筛选** - 查看全部/未完成/已完成任务
- 🧹 **批量操作** - 一键清除已完成或清空所有任务，带警告确认
- 💾 **数据持久化** - 使用 SQLite 数据库保存数据
- 🎨 **优雅 UI** - 渐变背景、平滑动画、响应式设计
- ⚠️ **智能提示** - 所有关键操作都有成功/失败/警告提示
- ♿ **无障碍性** - 支持屏幕阅读器，符合 WCAG 标准

## 🛠️ 技术栈

### 前端
- **React 18** - 现代化的前端框架
- **Vite** - 快速的构建工具
- **Axios** - HTTP 请求库
- **CSS3** - 现代化样式设计

### 后端
- **FastAPI** - 高性能的 Python Web 框架
- **SQLite** - 轻量级数据库
- **Pydantic** - 数据验证
- **Uvicorn** - ASGI 服务器

## 📦 项目结构

```
work3/
├── backend/                # 后端目录
│   ├── main.py            # FastAPI 主应用
│   ├── requirements.txt   # Python 依赖
│   ├── todos.db          # SQLite 数据库（自动生成）
│   └── .gitignore
│
├── frontend/              # 前端目录
│   ├── src/
│   │   ├── App.jsx       # 主应用组件
│   │   ├── App.css       # 应用样式
│   │   ├── main.jsx      # 入口文件
│   │   └── index.css     # 全局样式
│   ├── index.html        # HTML 模板
│   ├── vite.config.js    # Vite 配置
│   ├── package.json      # 前端依赖
│   └── .gitignore
│
├── database.sql          # 数据库表设计 SQL
└── README.md             # 项目文档
```

## 🚀 快速开始

### 环境要求

- **Node.js** >= 16.0
- **Python** >= 3.8
- **npm** 或 **yarn**

### 1️⃣ 安装后端依赖

```bash
cd backend

# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2️⃣ 启动后端服务

**方式一：使用启动脚本（推荐）**
```bash
# 在项目根目录（work3）下
# Windows:
start-backend.bat
# Mac/Linux:
./backend/start.sh
```

**方式二：手动启动**
```bash
# 在 backend 目录下，激活虚拟环境后
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

后端服务将运行在 `http://localhost:8000`

API 文档地址：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 3️⃣ 安装前端依赖

```bash
# 新开一个终端
cd frontend

# 安装依赖
npm install
```

### 4️⃣ 启动前端应用

**方式一：使用启动脚本（推荐）**
```bash
# 在项目根目录（work3）下
# Windows:
start-frontend.bat
# Mac/Linux:
./frontend/start.sh
```

**方式二：手动启动**
```bash
# 在 frontend 目录下
npm run dev
```

前端应用将运行在 `http://localhost:3000`
> **注意**: 前端使用 Vite 开发服务器，代码修改后会自动热重载

### 5️⃣ 访问应用

在浏览器打开 `http://localhost:3000`，开始使用待办事项应用！

## 📡 API 接口

### 获取所有待办事项
```
GET /api/todos?filter=all|active|completed
```

### 获取单个待办事项
```
GET /api/todos/{id}
```

### 创建待办事项
```
POST /api/todos
Body: { "text": "任务内容" }
```

### 更新待办事项
```
PUT /api/todos/{id}
Body: { "text": "新内容", "completed": true }
```

### 删除待办事项
```
DELETE /api/todos/{id}
```

### 清除已完成任务
```
DELETE /api/todos/clear/completed
```

### 清空所有任务
```
DELETE /api/todos/clear/all
```

### 获取统计信息
```
GET /api/stats
```

## 🗄️ 数据库设计

```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 UI 设计特点

- **渐变背景** - 紫色到粉紫色的流畅渐变
- **玻璃拟态** - 半透明卡片，带模糊效果
- **平滑动画** - 悬停、点击、滑入动画
- **响应式布局** - 适配移动端和桌面端
- **视觉反馈** - 所有交互都有即时视觉反馈

## 📱 响应式设计

应用完美支持以下设备：
- 📱 手机（320px+）
- 📱 平板（640px+）
- 💻 桌面（1024px+）

## 🔧 开发命令

### 后端开发
```bash
# 运行开发服务器（自动重载）
uvicorn main:app --reload

# 或直接运行
python main.py
```

### 前端开发
```bash
# 开发模式
npm run dev

# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

## 📝 使用说明

1. **添加任务**：在输入框输入任务内容，点击"添加"按钮
2. **标记完成**：点击任务前的圆圈或"完成"按钮
3. **取消完成**：再次点击已完成任务的圆圈或"取消完成"按钮
4. **删除任务**：点击任务右侧的"删除"按钮
5. **筛选任务**：点击"全部"、"未完成"、"已完成"按钮切换视图
6. **清除已完成**：点击底部"清除已完成"按钮
7. **清空所有**：点击底部"清空所有"按钮

## 🔧 关键技术修复

### SQLite 线程安全问题
在 FastAPI 异步环境中使用 SQLite 时，需要在连接时添加 `check_same_thread=False` 参数：
```python
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
```

### 数据类型转换
SQLite 的 BOOLEAN 类型实际存储为整数（0/1），需要在返回给前端前转换为布尔值：
```python
result['completed'] = bool(result['completed'])
```

### Pydantic V2 配置
使用新版 Pydantic 的 `ConfigDict` 替代旧的 `class Config`：
```python
from pydantic import BaseModel, ConfigDict

class Todo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
```

## 🐛 常见问题

### 1. 后端启动失败
- 确保已安装 Python 3.8+
- 检查端口 8000 是否被占用：`netstat -ano | findstr "8000"`
- 确认已正确安装依赖：`pip install -r requirements.txt`
- 使用 `uvicorn main:app` 而不是 `python main.py`

### 2. 前端无法连接后端
- 确保后端服务已启动（端口 8000）
- 检查后端运行在 `http://localhost:8000`
- 查看浏览器控制台网络错误信息
- 确认 Vite 代理配置正确

### 3. 数据无法保存
- 确保后端目录有写入权限
- 检查 `todos.db` 文件是否正常创建
- 查看后端控制台错误日志
- 确认 SQLite 连接配置正确

### 4. 空输入没有警告
- 前端已添加输入验证，空字段会弹出 `⚠️ 请输入任务内容！`
- 如未生效，请刷新浏览器（Vite 热重载）

## 🔐 安全性

- ✅ 输入内容自动 HTML 转义，防止 XSS 攻击
- ✅ API 参数验证，使用 Pydantic 模型
- ✅ SQL 查询使用参数化，防止 SQL 注入
- ✅ CORS 配置，限制跨域访问

## 📄 License

MIT License

## 👨‍💻 作者

**nikk909**  
📧 Email: yinghua253659@163.com  
🔗 GitHub: [@nikk909](https://github.com/nikk909)

基于现代化技术栈开发的全栈待办事项应用

---

**祝您使用愉快！** 🎉

如有问题，欢迎提 Issue 或 PR。

