"""
数据库初始化脚本
手动初始化数据库或重置数据库
"""
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "todos.db")


def init_database(add_sample_data=False):
    """
    初始化数据库
    
    Args:
        add_sample_data: 是否添加示例数据
    """
    print("🔧 开始初始化数据库...")
    print(f"📁 数据库路径: {DB_PATH}")
    
    # 连接数据库
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 创建表
    print("📝 创建 todos 表...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # 创建索引
    print("🔍 创建索引...")
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_todos_completed 
        ON todos(completed)
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_todos_created_at 
        ON todos(created_at DESC)
    """)
    
    # 添加示例数据
    if add_sample_data:
        print("📦 添加示例数据...")
        sample_todos = [
            ("完成项目文档", False),
            ("学习 React 新特性", False),
            ("代码审查", True),
            ("参加团队会议", False),
            ("编写单元测试", False),
            ("更新 API 文档", True),
        ]
        
        for text, completed in sample_todos:
            cursor.execute(
                "INSERT INTO todos (text, completed) VALUES (?, ?)",
                (text, 1 if completed else 0)
            )
        
        print(f"✅ 成功添加 {len(sample_todos)} 条示例数据")
    
    # 提交更改
    conn.commit()
    
    # 显示统计信息
    cursor.execute("SELECT COUNT(*) FROM todos")
    total = cursor.fetchone()[0]
    print(f"📊 当前数据库中共有 {total} 条任务")
    
    # 关闭连接
    conn.close()
    
    print("✅ 数据库初始化完成！")


def reset_database():
    """
    重置数据库（删除所有数据）
    """
    print("⚠️  警告：即将重置数据库，所有数据将被删除！")
    confirm = input("确认重置数据库？(yes/no): ")
    
    if confirm.lower() != 'yes':
        print("❌ 取消重置操作")
        return
    
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("🗑️  已删除原数据库文件")
    
    init_database(add_sample_data=True)


def show_stats():
    """显示数据库统计信息"""
    if not os.path.exists(DB_PATH):
        print("❌ 数据库文件不存在，请先初始化数据库")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n📊 数据库统计信息")
    print("=" * 50)
    
    # 总数
    cursor.execute("SELECT COUNT(*) FROM todos")
    total = cursor.fetchone()[0]
    print(f"总任务数: {total}")
    
    # 已完成
    cursor.execute("SELECT COUNT(*) FROM todos WHERE completed = 1")
    completed = cursor.fetchone()[0]
    print(f"已完成: {completed}")
    
    # 未完成
    cursor.execute("SELECT COUNT(*) FROM todos WHERE completed = 0")
    active = cursor.fetchone()[0]
    print(f"未完成: {active}")
    
    # 完成率
    if total > 0:
        completion_rate = (completed / total) * 100
        print(f"完成率: {completion_rate:.1f}%")
    
    print("=" * 50)
    
    # 显示最近的任务
    print("\n📝 最近的 5 条任务:")
    cursor.execute("""
        SELECT id, text, completed, created_at 
        FROM todos 
        ORDER BY created_at DESC 
        LIMIT 5
    """)
    
    for row in cursor.fetchall():
        status = "✅" if row[2] else "⏳"
        print(f"{status} [{row[0]}] {row[1]}")
    
    conn.close()


def export_data():
    """导出数据为 SQL 文件"""
    if not os.path.exists(DB_PATH):
        print("❌ 数据库文件不存在")
        return
    
    export_file = "todos_backup.sql"
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    with open(export_file, 'w', encoding='utf-8') as f:
        # 写入表结构
        f.write("-- 待办事项数据导出\n")
        f.write(f"-- 导出时间: {datetime.now().isoformat()}\n\n")
        
        # 获取所有数据
        cursor.execute("SELECT * FROM todos ORDER BY id")
        rows = cursor.fetchall()
        
        for row in rows:
            f.write(f"INSERT INTO todos (id, text, completed, created_at, updated_at) VALUES ")
            f.write(f"({row[0]}, '{row[1]}', {row[2]}, '{row[3]}', '{row[4]}');\n")
    
    conn.close()
    
    print(f"✅ 数据已导出到: {export_file}")


if __name__ == "__main__":
    """命令行交互"""
    import sys
    
    print("=" * 50)
    print("📦 待办事项应用 - 数据库管理工具")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "init":
            init_database(add_sample_data=False)
        elif command == "init-sample":
            init_database(add_sample_data=True)
        elif command == "reset":
            reset_database()
        elif command == "stats":
            show_stats()
        elif command == "export":
            export_data()
        else:
            print(f"❌ 未知命令: {command}")
            print("\n可用命令:")
            print("  init          - 初始化数据库（不含示例数据）")
            print("  init-sample   - 初始化数据库并添加示例数据")
            print("  reset         - 重置数据库")
            print("  stats         - 显示统计信息")
            print("  export        - 导出数据")
    else:
        # 交互式菜单
        print("\n请选择操作:")
        print("1. 初始化数据库")
        print("2. 初始化数据库（含示例数据）")
        print("3. 重置数据库")
        print("4. 显示统计信息")
        print("5. 导出数据")
        print("0. 退出")
        
        choice = input("\n请输入选项 (0-5): ")
        
        if choice == "1":
            init_database(add_sample_data=False)
        elif choice == "2":
            init_database(add_sample_data=True)
        elif choice == "3":
            reset_database()
        elif choice == "4":
            show_stats()
        elif choice == "5":
            export_data()
        elif choice == "0":
            print("👋 再见！")
        else:
            print("❌ 无效选项")

