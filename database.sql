-- 待办事项应用数据库表设计
-- SQLite 数据库

-- 创建待办事项表
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引以提高查询性能
CREATE INDEX IF NOT EXISTS idx_todos_completed ON todos(completed);
CREATE INDEX IF NOT EXISTS idx_todos_created_at ON todos(created_at DESC);

-- 插入示例数据（可选）
INSERT INTO todos (text, completed) VALUES
    ('完成项目文档', 0),
    ('学习 React 新特性', 0),
    ('代码审查', 1),
    ('参加团队会议', 0);

