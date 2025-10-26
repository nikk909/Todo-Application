"""简单测试数据库和 Pydantic 模型"""
import sqlite3
import os
from pydantic import BaseModel, ConfigDict

DB_PATH = os.path.join(os.path.dirname(__file__), "todos.db")

class Todo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    text: str
    completed: bool
    created_at: str
    updated_at: str

# 连接数据库
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# 插入一条测试数据
from datetime import datetime
now = datetime.now().isoformat()
cursor.execute(
    "INSERT INTO todos (text, completed, created_at, updated_at) VALUES (?, 0, ?, ?)",
    ("测试任务", now, now)
)
conn.commit()

# 查询数据
cursor.execute("SELECT id, text, completed, created_at, updated_at FROM todos")
rows = cursor.fetchall()

print(f"\n查询到 {len(rows)} 条数据:")
for row in rows:
    print(f"\nRow type: {type(row)}")
    print(f"Row dict: {dict(row)}")
    
    # 尝试创建 Pydantic 模型
    try:
        todo = Todo(**dict(row))
        print(f"✅ Pydantic 模型创建成功: {todo}")
    except Exception as e:
        print(f"❌ Pydantic 模型创建失败: {e}")

conn.close()
print("\n测试完成！")

