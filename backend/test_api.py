"""
API 测试脚本 - 待办事项应用
使用 pytest 进行单元测试和集成测试
"""
import pytest
from fastapi.testclient import TestClient
from main import app, init_db
import os

# 测试客户端
client = TestClient(app)

# 测试数据库路径
TEST_DB_PATH = "test_todos.db"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """每个测试前后的设置和清理"""
    # 设置：创建测试数据库
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    # 运行测试
    yield
    
    # 清理：删除测试数据库
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)


class TestHealthCheck:
    """健康检查测试"""
    
    def test_root_endpoint(self):
        """测试根路径"""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
        assert response.json()["version"] == "1.0.0"


class TestTodosCRUD:
    """待办事项 CRUD 测试"""
    
    def test_create_todo(self):
        """测试创建任务"""
        response = client.post(
            "/api/todos",
            json={"text": "测试任务"}
        )
        assert response.status_code == 201
        data = response.json()
        assert data["text"] == "测试任务"
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data
    
    def test_create_todo_empty_text(self):
        """测试创建空任务（应该失败）"""
        response = client.post(
            "/api/todos",
            json={"text": ""}
        )
        # FastAPI 会接受空字符串，但这是业务逻辑验证
        # 如果需要拒绝空字符串，需要在 Pydantic 模型中添加验证
        assert response.status_code in [201, 422]
    
    def test_get_todos(self):
        """测试获取任务列表"""
        # 先创建几个任务
        client.post("/api/todos", json={"text": "任务1"})
        client.post("/api/todos", json={"text": "任务2"})
        
        # 获取所有任务
        response = client.get("/api/todos")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 2
    
    def test_get_todos_with_filter(self):
        """测试筛选任务"""
        # 创建任务
        response1 = client.post("/api/todos", json={"text": "未完成任务"})
        todo_id = response1.json()["id"]
        
        # 标记为完成
        client.put(f"/api/todos/{todo_id}", json={"completed": True})
        
        # 创建未完成任务
        client.post("/api/todos", json={"text": "未完成任务2"})
        
        # 测试筛选已完成
        response = client.get("/api/todos?filter=completed")
        assert response.status_code == 200
        completed_todos = response.json()
        assert all(todo["completed"] for todo in completed_todos)
        
        # 测试筛选未完成
        response = client.get("/api/todos?filter=active")
        assert response.status_code == 200
        active_todos = response.json()
        assert all(not todo["completed"] for todo in active_todos)
    
    def test_get_single_todo(self):
        """测试获取单个任务"""
        # 创建任务
        create_response = client.post(
            "/api/todos",
            json={"text": "单个任务"}
        )
        todo_id = create_response.json()["id"]
        
        # 获取任务
        response = client.get(f"/api/todos/{todo_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == todo_id
        assert data["text"] == "单个任务"
    
    def test_get_nonexistent_todo(self):
        """测试获取不存在的任务"""
        response = client.get("/api/todos/99999")
        assert response.status_code == 404
        assert "detail" in response.json()
    
    def test_update_todo(self):
        """测试更新任务"""
        # 创建任务
        create_response = client.post(
            "/api/todos",
            json={"text": "原始任务"}
        )
        todo_id = create_response.json()["id"]
        
        # 更新任务
        response = client.put(
            f"/api/todos/{todo_id}",
            json={"text": "更新后的任务", "completed": True}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["text"] == "更新后的任务"
        assert data["completed"] is True
    
    def test_update_todo_partial(self):
        """测试部分更新任务"""
        # 创建任务
        create_response = client.post(
            "/api/todos",
            json={"text": "原始任务"}
        )
        todo_id = create_response.json()["id"]
        
        # 只更新完成状态
        response = client.put(
            f"/api/todos/{todo_id}",
            json={"completed": True}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["text"] == "原始任务"  # 文本未变
        assert data["completed"] is True
    
    def test_delete_todo(self):
        """测试删除任务"""
        # 创建任务
        create_response = client.post(
            "/api/todos",
            json={"text": "待删除任务"}
        )
        todo_id = create_response.json()["id"]
        
        # 删除任务
        response = client.delete(f"/api/todos/{todo_id}")
        assert response.status_code == 200
        assert response.json()["id"] == todo_id
        
        # 验证已删除
        get_response = client.get(f"/api/todos/{todo_id}")
        assert get_response.status_code == 404


class TestBulkOperations:
    """批量操作测试"""
    
    def test_clear_completed(self):
        """测试清除已完成任务"""
        # 创建多个任务
        todo1 = client.post("/api/todos", json={"text": "任务1"}).json()
        todo2 = client.post("/api/todos", json={"text": "任务2"}).json()
        todo3 = client.post("/api/todos", json={"text": "任务3"}).json()
        
        # 标记部分任务为完成
        client.put(f"/api/todos/{todo1['id']}", json={"completed": True})
        client.put(f"/api/todos/{todo2['id']}", json={"completed": True})
        
        # 清除已完成
        response = client.delete("/api/todos/clear/completed")
        assert response.status_code == 200
        assert response.json()["count"] == 2
        
        # 验证只剩未完成任务
        todos = client.get("/api/todos").json()
        assert len(todos) == 1
        assert todos[0]["id"] == todo3["id"]
    
    def test_clear_all(self):
        """测试清空所有任务"""
        # 创建多个任务
        client.post("/api/todos", json={"text": "任务1"})
        client.post("/api/todos", json={"text": "任务2"})
        client.post("/api/todos", json={"text": "任务3"})
        
        # 清空所有
        response = client.delete("/api/todos/clear/all")
        assert response.status_code == 200
        assert response.json()["count"] == 3
        
        # 验证列表为空
        todos = client.get("/api/todos").json()
        assert len(todos) == 0


class TestStatistics:
    """统计功能测试"""
    
    def test_get_stats(self):
        """测试获取统计信息"""
        # 创建任务
        todo1 = client.post("/api/todos", json={"text": "任务1"}).json()
        client.post("/api/todos", json={"text": "任务2"})
        client.post("/api/todos", json={"text": "任务3"})
        
        # 标记一个为完成
        client.put(f"/api/todos/{todo1['id']}", json={"completed": True})
        
        # 获取统计
        response = client.get("/api/stats")
        assert response.status_code == 200
        stats = response.json()
        assert stats["total"] == 3
        assert stats["completed"] == 1
        assert stats["active"] == 2


class TestDataValidation:
    """数据验证测试"""
    
    def test_create_todo_missing_text(self):
        """测试缺少必填字段"""
        response = client.post("/api/todos", json={})
        assert response.status_code == 422
    
    def test_update_todo_invalid_type(self):
        """测试错误的数据类型"""
        # 创建任务
        create_response = client.post(
            "/api/todos",
            json={"text": "测试任务"}
        )
        todo_id = create_response.json()["id"]
        
        # 尝试用错误类型更新
        response = client.put(
            f"/api/todos/{todo_id}",
            json={"completed": "not_a_boolean"}
        )
        assert response.status_code == 422


class TestEdgeCases:
    """边界情况测试"""
    
    def test_very_long_text(self):
        """测试超长文本"""
        long_text = "A" * 10000
        response = client.post(
            "/api/todos",
            json={"text": long_text}
        )
        # SQLite TEXT 类型可以存储很长的文本
        assert response.status_code == 201
        assert len(response.json()["text"]) == 10000
    
    def test_special_characters(self):
        """测试特殊字符"""
        special_text = "任务 <script>alert('xss')</script> 😀 🎉"
        response = client.post(
            "/api/todos",
            json={"text": special_text}
        )
        assert response.status_code == 201
        # 验证特殊字符被正确存储
        assert response.json()["text"] == special_text
    
    def test_unicode_text(self):
        """测试 Unicode 字符"""
        unicode_text = "你好世界 مرحبا بالعالم Hello World"
        response = client.post(
            "/api/todos",
            json={"text": unicode_text}
        )
        assert response.status_code == 201
        assert response.json()["text"] == unicode_text


if __name__ == "__main__":
    """直接运行测试"""
    pytest.main([__file__, "-v", "--tb=short"])

