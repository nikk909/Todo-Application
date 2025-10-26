# 待办事项应用 - 前端文档

## 📋 目录

1. [项目简介](#项目简介)
2. [技术栈](#技术栈)
3. [快速开始](#快速开始)
4. [功能说明](#功能说明)
5. [API 集成](#api-集成)
6. [组件结构](#组件结构)
7. [样式设计](#样式设计)
8. [开发指南](#开发指南)
9. [构建部署](#构建部署)
10. [故障排查](#故障排查)

---

## 项目简介

基于 React 18 + Vite 构建的现代化待办事项管理前端应用，提供直观的用户界面和流畅的交互体验。

### 核心特性

- ✅ **React 18**: 最新的 React 版本，函数式组件 + Hooks
- ✅ **Vite**: 极速的开发服务器和构建工具
- ✅ **Axios**: 强大的 HTTP 客户端
- ✅ **响应式设计**: 完美适配移动端和桌面端
- ✅ **优雅动画**: 平滑的过渡和交互效果
- ✅ **渐变主题**: 紫色系渐变背景，现代美观

---

## 技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| React | 18.2.0 | UI 框架 |
| Vite | 5.0.11 | 构建工具 |
| Axios | 1.6.5 | HTTP 客户端 |
| CSS3 | - | 样式设计 |
| JavaScript | ES6+ | 编程语言 |

---

## 快速开始

### 前提条件

- Node.js >= 16.0
- npm 或 yarn
- 后端服务运行在 `http://localhost:8000`

### 安装依赖

```bash
npm install
# 或
yarn install
```

### 启动开发服务器

```bash
npm run dev
# 或
yarn dev
```

服务将运行在 `http://localhost:3000`

### 构建生产版本

```bash
npm run build
# 或
yarn build
```

构建产物位于 `dist/` 目录

### 预览生产版本

```bash
npm run preview
# 或
yarn preview
```

---

## 功能说明

### 1. 任务管理

#### 添加任务
- 在输入框输入任务内容
- 点击"添加"按钮或按 Enter 键
- 任务自动添加到列表顶部

#### 查看任务
- 任务列表按创建时间倒序排列
- 显示任务内容和完成状态
- 支持滑入动画效果

#### 标记完成/取消完成
- 点击任务前的圆形复选框
- 或点击"完成"/"取消完成"按钮
- 已完成任务显示划线效果

#### 删除任务
- 点击"删除"按钮
- 弹出确认对话框
- 确认后从列表移除

### 2. 任务筛选

- **全部**: 显示所有任务
- **未完成**: 只显示未完成的任务
- **已完成**: 只显示已完成的任务

### 3. 批量操作

#### 清除已完成
- 点击"清除已完成"按钮
- 确认后删除所有已完成任务

#### 清空所有
- 点击"清空所有"按钮
- 确认后删除所有任务

### 4. 统计信息

- 顶部显示当前任务总数
- 根据筛选条件动态更新

---

## API 集成

### API 配置

```javascript
const API_BASE = '/api'  // Vite 代理到 http://localhost:8000
```

### 接口调用

#### 1. 获取任务列表

```javascript
const fetchTodos = async (filter = 'all') => {
  const response = await axios.get(`${API_BASE}/todos`, {
    params: filter !== 'all' ? { filter } : {}
  })
  setTodos(response.data)
}
```

#### 2. 创建任务

```javascript
await axios.post(`${API_BASE}/todos`, { text })
```

#### 3. 更新任务

```javascript
await axios.put(`${API_BASE}/todos/${id}`, {
  completed: !currentCompleted
})
```

#### 4. 删除任务

```javascript
await axios.delete(`${API_BASE}/todos/${id}`)
```

#### 5. 清除已完成

```javascript
await axios.delete(`${API_BASE}/todos/clear/completed`)
```

#### 6. 清空所有

```javascript
await axios.delete(`${API_BASE}/todos/clear/all`)
```

### 错误处理

```javascript
try {
  // API 调用
} catch (error) {
  console.error('操作失败:', error)
  alert('操作失败，请重试')
}
```

---

## 组件结构

### 应用结构

```
App.jsx
├── Header (标题区域)
│   └── <h1>我的待办事项</h1>
│
├── AddSection (添加任务区域)
│   └── <form>
│       ├── <input> 输入框
│       └── <button> 添加按钮
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
│   │   └── TodoItem[] (任务项列表)
│   │       ├── Checkbox (复选框)
│   │       ├── Text (任务内容)
│   │       └── Actions (操作按钮)
│   │           ├── CompleteButton (完成按钮)
│   │           └── DeleteButton (删除按钮)
│   └── EmptyState (空状态提示)
│
└── ActionSection (底部操作区域)
    ├── ClearCompletedButton (清除已完成)
    └── ClearAllButton (清空所有)
```

### 状态管理

```javascript
const [todos, setTodos] = useState([])              // 任务列表
const [inputValue, setInputValue] = useState('')    // 输入框值
const [currentFilter, setCurrentFilter] = useState('all') // 筛选条件
const [loading, setLoading] = useState(false)       // 加载状态
```

### 生命周期

```javascript
// 组件挂载和筛选条件变化时获取数据
useEffect(() => {
  fetchTodos(currentFilter)
}, [currentFilter])
```

---

## 样式设计

### 设计理念

继承自 work2 的设计风格：

- **渐变背景**: 紫色 (#667eea) → 粉紫色 (#764ba2)
- **玻璃拟态**: 半透明白色卡片，毛玻璃效果
- **圆角设计**: 统一使用 8-12px 圆角
- **阴影效果**: 多层次阴影，增加立体感
- **平滑动画**: 所有交互都有过渡效果

### 颜色方案

```css
/* 主色调 */
--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
--success-color: #48bb78;  /* 绿色 - 成功 */
--danger-color: #fc8181;   /* 红色 - 危险 */
--text-color: #2d3748;     /* 深灰 - 文字 */
```

### 关键样式

#### 1. 渐变背景
```css
body {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}
```

#### 2. 玻璃拟态卡片
```css
.card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
```

#### 3. 悬停效果
```css
.todo-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}
```

#### 4. 滑入动画
```css
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## 开发指南

### 项目结构

```
frontend/
├── src/
│   ├── main.jsx          # 应用入口
│   ├── App.jsx           # 主组件
│   ├── App.css           # 应用样式
│   └── index.css         # 全局样式
├── index.html            # HTML 模板
├── vite.config.js        # Vite 配置
├── package.json          # 依赖配置
└── README_FRONTEND.md    # 本文档
```

### 添加新功能

#### 1. 添加新的状态

```javascript
const [newState, setNewState] = useState(initialValue)
```

#### 2. 添加新的 API 调用

```javascript
const newApiCall = async () => {
  try {
    const response = await axios.get(`${API_BASE}/new-endpoint`)
    // 处理响应
  } catch (error) {
    console.error('错误:', error)
  }
}
```

#### 3. 添加新的组件

```javascript
const NewComponent = () => {
  return (
    <div className="new-component">
      {/* 组件内容 */}
    </div>
  )
}
```

### 代码规范

- 使用函数式组件
- 使用 Hooks 管理状态
- 组件名使用大驼峰命名
- 变量名使用小驼峰命名
- 添加适当的注释

### 调试技巧

#### 1. 查看网络请求

```javascript
console.log('API Response:', response.data)
```

#### 2. React DevTools

安装 React Developer Tools 浏览器插件

#### 3. 查看状态变化

```javascript
console.log('Current State:', todos, currentFilter)
```

---

## 构建部署

### 开发环境

```bash
npm run dev
```

- 启用热模块替换 (HMR)
- 快速重载
- Source Maps 支持

### 生产构建

```bash
npm run build
```

构建优化：
- 代码压缩
- Tree Shaking
- 资源优化
- 输出到 `dist/` 目录

### 预览构建结果

```bash
npm run preview
```

在 `http://localhost:4173` 预览生产版本

### 部署到静态服务器

#### 1. Nginx

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 2. Apache

```apache
<VirtualHost *:80>
    ServerName your-domain.com
    DocumentRoot /path/to/dist
    
    <Directory /path/to/dist>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
        
        RewriteEngine On
        RewriteBase /
        RewriteRule ^index\.html$ - [L]
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteCond %{REQUEST_FILENAME} !-d
        RewriteRule . /index.html [L]
    </Directory>
    
    ProxyPass /api http://localhost:8000/api
    ProxyPassReverse /api http://localhost:8000/api
</VirtualHost>
```

#### 3. Vercel / Netlify

直接连接 Git 仓库，自动部署

---

## 故障排查

### 问题 1: 无法连接后端

**症状**: 提示"获取数据失败，请检查后端服务是否启动"

**解决方案**:
1. 确认后端服务运行在 `http://localhost:8000`
2. 检查 Vite 代理配置 (`vite.config.js`)
3. 查看浏览器控制台网络请求

```javascript
// vite.config.js
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
})
```

### 问题 2: 端口被占用

**症状**: `Port 3000 is in use`

**解决方案**:
```bash
# 使用其他端口
npm run dev -- --port 3001

# 或修改 vite.config.js
export default defineConfig({
  server: {
    port: 3001
  }
})
```

### 问题 3: 依赖安装失败

**症状**: `npm install` 报错

**解决方案**:
```bash
# 清除缓存
npm cache clean --force

# 删除 node_modules 和 package-lock.json
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

### 问题 4: 白屏问题

**症状**: 页面显示空白

**解决方案**:
1. 检查浏览器控制台错误
2. 确认 `index.html` 中的 `<div id="root"></div>` 存在
3. 检查 `main.jsx` 是否正确引入
4. 清除浏览器缓存 (Ctrl + Shift + Delete)

### 问题 5: 样式不生效

**症状**: 页面布局错乱

**解决方案**:
1. 确认 CSS 文件正确导入
2. 检查类名是否正确
3. 清除浏览器缓存
4. 重启开发服务器

---

## 性能优化

### 1. 代码分割

```javascript
// 懒加载组件
const LazyComponent = React.lazy(() => import('./LazyComponent'))

<Suspense fallback={<div>Loading...</div>}>
  <LazyComponent />
</Suspense>
```

### 2. 避免不必要的渲染

```javascript
// 使用 React.memo
const TodoItem = React.memo(({ todo, onToggle, onDelete }) => {
  // ...
})
```

### 3. 使用 useCallback

```javascript
const handleToggle = useCallback((id, completed) => {
  toggleTodo(id, completed)
}, [])
```

### 4. 使用 useMemo

```javascript
const filteredTodos = useMemo(() => {
  return todos.filter(todo => /* 筛选逻辑 */)
}, [todos, currentFilter])
```

---

## 响应式设计

### 断点设置

```css
/* 移动端 */
@media (max-width: 640px) {
  /* 样式调整 */
}

/* 平板 */
@media (min-width: 641px) and (max-width: 1024px) {
  /* 样式调整 */
}

/* 桌面端 */
@media (min-width: 1025px) {
  /* 样式调整 */
}
```

### 移动端优化

- 表单垂直排列
- 按钮全宽显示
- 字体大小适配
- 触摸友好的点击区域

---

## 浏览器支持

| 浏览器 | 版本 |
|--------|------|
| Chrome | 最新版 |
| Firefox | 最新版 |
| Safari | 最新版 |
| Edge | 最新版 |

---

## 开发工具推荐

- **VS Code**: 推荐的代码编辑器
- **React DevTools**: React 调试工具
- **Vite DevTools**: Vite 开发工具
- **ESLint**: 代码检查
- **Prettier**: 代码格式化

---

## 相关资源

- [React 官方文档](https://react.dev/)
- [Vite 官方文档](https://vitejs.dev/)
- [Axios 文档](https://axios-http.com/)
- [CSS-Tricks](https://css-tricks.com/)

---

## 常见问题 (FAQ)

### Q: 如何修改主题颜色？

A: 编辑 `App.css` 中的颜色变量：
```css
body {
  background: linear-gradient(135deg, #your-color-1, #your-color-2);
}
```

### Q: 如何添加新的筛选条件？

A: 在 `FilterButtons` 区域添加新按钮，并更新 `handleFilter` 函数。

### Q: 如何更改默认端口？

A: 修改 `vite.config.js`:
```javascript
export default defineConfig({
  server: {
    port: 3001  // 修改为你想要的端口
  }
})
```

---

## 许可证

MIT License

---

## 联系方式

如有问题，请查看主项目 README 或提交 Issue。

---

**文档版本**: 1.0.0  
**最后更新**: 2025-10-26

**Happy Coding! 🎉**

