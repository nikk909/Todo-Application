"""测试数据库连接和初始化"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "todos.db")

print(f"数据库路径: {DB_PATH}")
print(f"数据库文件存在: {os.path.exists(DB_PATH)}")

# 连接数据库
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# 查询表结构
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"\n现有表: {[t['name'] for t in tables]}")

if 'todos' in [t['name'] for t in tables]:
    # 查询表字段
    cursor.execute("PRAGMA table_info(todos);")
    columns = cursor.fetchall()
    print(f"\ntodos 表字段:")
    for col in columns:
        print(f"  - {dict(col)}")
    
    # 查询数据
    cursor.execute("SELECT * FROM todos;")
    rows = cursor.fetchall()
    print(f"\n当前数据数量: {len(rows)}")
    for row in rows:
        print(f"  {dict(row)}")
else:
    print("\n❌ todos 表不存在！")

conn.close()
print("\n✅ 测试完成")

