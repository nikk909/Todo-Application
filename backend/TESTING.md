# 后端 API 测试指南

## 🧪 测试方式

### 1. 自动化测试（推荐）

#### 运行全部测试
```bash
# 安装测试依赖
pip install -r requirements-test.txt

# 运行测试
pytest test_api.py -v
```

#### 测试结果示例
```
test_api.py::TestHealthCheck::test_root_endpoint PASSED
test_api.py::TestTodosCRUD::test_create_todo PASSED
test_api.py::TestTodosCRUD::test_get_todos PASSED
...
======================== 15 passed in 2.34s ========================
```

### 2. Swagger UI 测试（交互式）

1. 启动后端服务：`python main.py`
2. 访问：http://localhost:8000/docs
3. 点击任意接口展开
4. 点击 "Try it out" 按钮
5. 填写参数
6. 点击 "Execute" 执行

**优点**：
- ✅ 可视化界面
- ✅ 自动生成请求示例
- ✅ 实时查看响应
- ✅ 支持所有接口

### 3. Postman 测试

1. 导入 `postman_collection.json`
2. 设置 `base_url` 变量为 `http://localhost:8000`
3. 按顺序执行请求

### 4. curl 命令行测试

#### 创建任务
```bash
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"text":"测试任务"}'
```

#### 获取所有任务
```bash
curl http://localhost:8000/api/todos
```

#### 更新任务（标记完成）
```bash
curl -X PUT http://localhost:8000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'
```

#### 删除任务
```bash
curl -X DELETE http://localhost:8000/api/todos/1
```

---

## 📋 完整测试流程

### 步骤 1: 启动服务
```bash
python main.py
```

### 步骤 2: 健康检查
```bash
curl http://localhost:8000/
```

### 步骤 3: 创建任务
```bash
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"text":"完成文档"}'
  
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"text":"编写测试"}'
```

### 步骤 4: 获取任务列表
```bash
curl http://localhost:8000/api/todos
```

### 步骤 5: 标记任务完成
```bash
curl -X PUT http://localhost:8000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'
```

### 步骤 6: 筛选已完成任务
```bash
curl http://localhost:8000/api/todos?filter=completed
```

### 步骤 7: 获取统计信息
```bash
curl http://localhost:8000/api/stats
```

### 步骤 8: 清除已完成
```bash
curl -X DELETE http://localhost:8000/api/todos/clear/completed
```

---

## 🔍 测试覆盖范围

### ✅ 已测试功能

- [x] 健康检查接口
- [x] 创建任务（正常 & 边界情况）
- [x] 获取任务列表（全部 / 筛选）
- [x] 获取单个任务
- [x] 更新任务（全量 & 部分）
- [x] 删除任务
- [x] 清除已完成任务
- [x] 清空所有任务
- [x] 获取统计信息
- [x] 数据验证（缺失字段 / 类型错误）
- [x] 边界测试（超长文本 / 特殊字符 / Unicode）
- [x] 错误处理（404 / 422）

### 测试用例数量

- **健康检查**: 1 个
- **CRUD 操作**: 8 个
- **批量操作**: 2 个
- **统计功能**: 1 个
- **数据验证**: 2 个
- **边界测试**: 3 个

**总计**: 17 个测试用例

---

## 🎯 快速验证脚本

创建 `quick_test.sh`:
```bash
#!/bin/bash
BASE_URL="http://localhost:8000"

echo "1️⃣  健康检查..."
curl -s $BASE_URL/ | jq

echo -e "\n2️⃣  创建任务..."
curl -s -X POST $BASE_URL/api/todos \
  -H "Content-Type: application/json" \
  -d '{"text":"测试任务1"}' | jq

echo -e "\n3️⃣  获取任务列表..."
curl -s $BASE_URL/api/todos | jq

echo -e "\n4️⃣  获取统计..."
curl -s $BASE_URL/api/stats | jq

echo -e "\n✅ 测试完成！"
```

运行:
```bash
chmod +x quick_test.sh
./quick_test.sh
```

---

## 📊 性能测试

### 使用 Apache Bench
```bash
# 测试健康检查接口
ab -n 1000 -c 10 http://localhost:8000/

# 测试获取任务列表
ab -n 1000 -c 10 http://localhost:8000/api/todos
```

### 使用 wrk
```bash
# 安装 wrk
# Linux: sudo apt-get install wrk
# Mac: brew install wrk

# 压力测试
wrk -t4 -c100 -d30s http://localhost:8000/api/todos
```

---

## 🐛 常见测试问题

### 问题 1: 测试失败 - 连接被拒绝

**原因**: 后端服务未启动

**解决**: 
```bash
python main.py
```

### 问题 2: 测试数据库冲突

**原因**: 测试使用了生产数据库

**解决**: 测试会自动使用 `test_todos.db`，无需担心

### 问题 3: pytest 未找到

**原因**: 未安装测试依赖

**解决**:
```bash
pip install -r requirements-test.txt
```

---

## 📝 测试最佳实践

1. ✅ **每次修改代码后运行测试**
2. ✅ **使用 Swagger UI 验证新接口**
3. ✅ **保持测试用例更新**
4. ✅ **测试边界情况和异常**
5. ✅ **使用真实场景数据**

---

## 🔗 相关资源

- [pytest 文档](https://docs.pytest.org/)
- [FastAPI 测试文档](https://fastapi.tiangolo.com/tutorial/testing/)
- [Postman 文档](https://learning.postman.com/)

---

**Happy Testing! 🎉**

