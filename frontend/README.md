# 前端应用

React + Vite 待办事项前端应用。

## 快速开始

### 1. 安装依赖

```bash
npm install
# 或
yarn install
```

### 2. 启动开发服务器

```bash
npm run dev
# 或
yarn dev
```

应用将运行在 `http://localhost:3000`

### 3. 构建生产版本

```bash
npm run build
# 或
yarn build
```

## 技术栈

- **React 18** - UI 框架
- **Vite** - 构建工具
- **Axios** - HTTP 客户端
- **CSS3** - 样式设计

## 设计风格

继承自 work2 的设计风格：
- 渐变紫色背景
- 玻璃拟态卡片
- 平滑动画效果
- 响应式布局

## 配置

在 `vite.config.js` 中配置了：
- 开发服务器端口：3000
- API 代理：`/api` -> `http://localhost:8000`

确保后端服务运行在 8000 端口。

