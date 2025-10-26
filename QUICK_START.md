# 🚀 快速启动指南

## 📋 前提条件

确保已安装以下软件：

- ✅ **Python** 3.8+ ([下载](https://www.python.org/downloads/))
- ✅ **Node.js** 16.0+ ([下载](https://nodejs.org/))
- ✅ **npm** 或 **yarn** (Node.js 自带)

---

## ⚡ 最快启动方式（推荐）

### 方式 1: 使用启动脚本

#### Windows

打开两个终端窗口：

**终端 1 - 启动后端**:
```bash
cd work3\backend
start.bat
```

**终端 2 - 启动前端**:
```bash
cd work3\frontend
start.bat
```

#### Linux/Mac

打开两个终端窗口：

**终端 1 - 启动后端**:
```bash
cd work3/backend
chmod +x start.sh
./start.sh
```

**终端 2 - 启动前端**:
```bash
cd work3/frontend
chmod +x start.sh
./start.sh
```

### 方式 2: 手动启动

#### 第一步：启动后端

```bash
# 进入后端目录
cd work3/backend

# 创建虚拟环境（首次）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖（首次）
pip install -r requirements.txt

# 启动后端服务
python main.py
```

**后端运行**: http://localhost:8000

#### 第二步：启动前端（新开终端）

```bash
# 进入前端目录
cd work3/frontend

# 安装依赖（首次）
npm install

# 启动前端服务
npm run dev
```

**前端运行**: http://localhost:3000

---

## 🎯 访问应用

启动完成后，访问以下地址：

| 服务 | 地址 | 说明 |
|------|------|------|
| **前端应用** | http://localhost:3000 | 待办事项界面 |
| **后端 API** | http://localhost:8000 | API 服务 |
| **API 文档** | http://localhost:8000/docs | Swagger UI |
| **API 文档 2** | http://localhost:8000/redoc | ReDoc |

---

## ✅ 验证是否成功

### 1. 检查后端

访问 http://localhost:8000，应该看到：

```json
{
  "message": "待办事项 API 服务正常运行",
  "version": "1.0.0"
}
```

### 2. 检查前端

访问 http://localhost:3000，应该看到：

- ✅ 紫色渐变背景
- ✅ "我的待办事项"标题
- ✅ 输入框和添加按钮
- ✅ 任务列表区域

### 3. 测试功能

1. 在输入框输入"测试任务"
2. 点击"添加"按钮
3. 任务出现在列表中
4. ✅ 功能正常！

---

## 🐛 常见问题

### 问题 1: 端口被占用

#### 后端端口 8000 被占用

**Windows**:
```bash
netstat -ano | findstr :8000
taskkill /PID <进程ID> /F
```

**Linux/Mac**:
```bash
lsof -i :8000
kill -9 <进程ID>
```

#### 前端端口 3000 被占用

修改端口启动：
```bash
npm run dev -- --port 3001
```

### 问题 2: Python 虚拟环境激活失败

**Windows PowerShell 权限问题**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 问题 3: npm install 很慢

使用国内镜像：
```bash
npm config set registry https://registry.npmmirror.com
npm install
```

### 问题 4: 前端无法连接后端

1. 确认后端已启动（访问 http://localhost:8000）
2. 检查控制台是否有 CORS 错误
3. 重启前端服务

### 问题 5: 数据库文件权限错误

**Linux/Mac**:
```bash
chmod 666 backend/todos.db
```

---

## 📚 下一步

### 🎓 学习资源

1. **后端文档**: `backend/README_BACKEND.md`
2. **前端文档**: `frontend/README_FRONTEND.md`
3. **API 测试**: `backend/TESTING.md`
4. **集成测试**: `frontend/INTEGRATION_TESTING.md`
5. **技术架构**: `TECHNICAL_ARCHITECTURE.md`

### 🧪 测试应用

#### 后端 API 测试

访问 Swagger UI: http://localhost:8000/docs

1. 展开任意接口
2. 点击 "Try it out"
3. 填写参数
4. 点击 "Execute"
5. 查看响应结果

#### 前端功能测试

按照 `frontend/INTEGRATION_TESTING.md` 执行完整测试。

### 🎨 自定义主题

编辑 `frontend/src/App.css` 修改颜色：

```css
body {
  /* 修改背景渐变 */
  background: linear-gradient(135deg, #your-color-1, #your-color-2);
}
```

### 📝 添加示例数据

```bash
cd backend
python init_db.py init-sample
```

---

## 🎯 核心功能演示

### 1. 添加任务

1. 在输入框输入任务内容
2. 按 Enter 或点击"添加"按钮
3. ✅ 任务添加到列表

### 2. 标记完成

方式一：点击任务前的圆圈  
方式二：点击"完成"按钮

### 3. 筛选任务

- 点击"全部" - 显示所有任务
- 点击"未完成" - 只显示未完成
- 点击"已完成" - 只显示已完成

### 4. 删除任务

- 鼠标悬停在任务上
- 点击"删除"按钮
- 确认删除

### 5. 批量操作

- **清除已完成** - 删除所有已完成任务
- **清空所有** - 删除所有任务

---

## 🎬 完整操作流程

```
1. 启动后端服务 (http://localhost:8000)
   ↓
2. 启动前端服务 (http://localhost:3000)
   ↓
3. 访问前端应用
   ↓
4. 添加几个任务
   ↓
5. 标记部分任务为完成
   ↓
6. 测试筛选功能
   ↓
7. 测试删除功能
   ↓
8. 测试批量操作
   ↓
9. ✅ 体验完整功能！
```

---

## 📞 获取帮助

### 查看文档

- 主 README: `README.md`
- 后端文档: `backend/README_BACKEND.md`
- 前端文档: `frontend/README_FRONTEND.md`
- 技术架构: `TECHNICAL_ARCHITECTURE.md`

### 查看日志

**后端日志**: 查看后端终端输出  
**前端日志**: 打开浏览器控制台 (F12)

### 常用命令

```bash
# 后端
python main.py          # 启动服务
pytest test_api.py -v   # 运行测试
python init_db.py stats # 查看数据库统计

# 前端
npm run dev             # 启动开发服务器
npm run build           # 构建生产版本
npm run preview         # 预览生产版本
```

---

## 🎉 恭喜！

您已经成功启动了待办事项应用！

### 接下来可以：

1. ✅ 体验所有功能
2. ✅ 阅读详细文档
3. ✅ 自定义主题样式
4. ✅ 添加新功能
5. ✅ 部署到生产环境

---

**祝您使用愉快！** 🚀

如有问题，请查看相关文档或提交 Issue。

