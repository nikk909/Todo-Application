import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const API_BASE = '/api'

function App() {
  const [todos, setTodos] = useState([])
  const [inputValue, setInputValue] = useState('')
  const [currentFilter, setCurrentFilter] = useState('all')
  const [loading, setLoading] = useState(false)
  const [stats, setStats] = useState({ total: 0, active: 0, completed: 0 })

  // 获取待办事项
  const fetchTodos = async (filter = 'all') => {
    try {
      setLoading(true)
      const response = await axios.get(`${API_BASE}/todos`, {
        params: filter !== 'all' ? { filter } : {}
      })
      setTodos(response.data)
      
      // 同时获取统计信息
      const statsResponse = await axios.get(`${API_BASE}/stats`)
      setStats(statsResponse.data)
    } catch (error) {
      console.error('获取待办事项失败:', error)
      alert('获取数据失败，请检查后端服务是否启动')
    } finally {
      setLoading(false)
    }
  }

  // 组件挂载时获取数据
  useEffect(() => {
    fetchTodos(currentFilter)
  }, [currentFilter])

  // 添加待办事项
  const handleAddTodo = async (e) => {
    e.preventDefault()
    const text = inputValue.trim()
    
    // 验证输入不为空
    if (text === '') {
      alert('⚠️ 请输入任务内容！')
      return
    }

    try {
      await axios.post(`${API_BASE}/todos`, { text })
      setInputValue('')
      fetchTodos(currentFilter)
      alert('✅ 任务添加成功！')
    } catch (error) {
      console.error('添加失败:', error)
      alert('❌ 添加失败，请重试')
    }
  }

  // 切换完成状态
  const toggleTodo = async (id, currentCompleted) => {
    try {
      await axios.put(`${API_BASE}/todos/${id}`, {
        completed: !currentCompleted
      })
      fetchTodos(currentFilter)
    } catch (error) {
      console.error('更新失败:', error)
    }
  }

  // 删除待办事项
  const deleteTodo = async (id) => {
    if (!confirm('⚠️ 确定要删除这个任务吗？\n删除后无法恢复！')) return
    
    try {
      await axios.delete(`${API_BASE}/todos/${id}`)
      fetchTodos(currentFilter)
      alert('✅ 任务已删除')
    } catch (error) {
      console.error('删除失败:', error)
      alert('❌ 删除失败，请重试')
    }
  }

  // 切换筛选
  const handleFilter = (filter) => {
    setCurrentFilter(filter)
  }

  // 清除已完成
  const clearCompleted = async () => {
    if (!confirm('⚠️ 确定要清除所有已完成的任务吗？\n此操作无法恢复！')) return
    
    try {
      await axios.delete(`${API_BASE}/todos/clear/completed`)
      fetchTodos(currentFilter)
      alert('✅ 已完成的任务已清除')
    } catch (error) {
      console.error('清除失败:', error)
      alert('❌ 清除失败，请重试')
    }
  }

  // 清空所有
  const clearAll = async () => {
    if (!confirm('⚠️ 警告！确定要清空所有任务吗？\n此操作不可恢复！')) return
    
    try {
      await axios.delete(`${API_BASE}/todos/clear/all`)
      fetchTodos(currentFilter)
      alert('✅ 所有任务已清空')
    } catch (error) {
      console.error('清空失败:', error)
      alert('❌ 清空失败，请重试')
    }
  }

  return (
    <div className="container">
      <header>
        <h1>我的待办事项</h1>
      </header>
      
      <main>
        {/* 添加任务表单 */}
        <section className="add-section">
          <form onSubmit={handleAddTodo} autoComplete="off">
            <input
              type="text"
              id="new-todo"
              placeholder="请输入新任务..."
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              disabled={loading}
              aria-label="新任务输入框"
              title="请输入任务内容"
            />
            <button type="submit" className="btn-add" disabled={loading}>
              <span>添加</span>
              <span className="add-icon">+</span>
            </button>
          </form>
        </section>

        {/* 任务统计和筛选 */}
        <section className="control-section">
          <div className="task-stats">
            <span className="stats-text">
              共 <strong id="total-count">{stats.total}</strong> 项任务
              {currentFilter === 'active' && ` (未完成: ${stats.active})`}
              {currentFilter === 'completed' && ` (已完成: ${stats.completed})`}
            </span>
          </div>
          <div className="filter-buttons">
            <button
              className={`filter-btn ${currentFilter === 'all' ? 'active' : ''}`}
              onClick={() => handleFilter('all')}
            >
              全部
            </button>
            <button
              className={`filter-btn ${currentFilter === 'active' ? 'active' : ''}`}
              onClick={() => handleFilter('active')}
            >
              未完成
            </button>
            <button
              className={`filter-btn ${currentFilter === 'completed' ? 'active' : ''}`}
              onClick={() => handleFilter('completed')}
            >
              已完成
            </button>
          </div>
        </section>

        {/* 任务列表 */}
        <section className="list-section">
          <ul id="todo-list">
            {todos.map((todo) => (
              <li
                key={todo.id}
                className={`todo-item ${todo.completed ? 'completed' : ''}`}
              >
                <div
                  className="todo-checkbox"
                  onClick={() => toggleTodo(todo.id, todo.completed)}
                ></div>
                <span className="todo-text">{todo.text}</span>
                <div className="todo-actions">
                  <button
                    className="btn-complete"
                    onClick={() => toggleTodo(todo.id, todo.completed)}
                  >
                    {todo.completed ? '取消完成' : '完成'}
                  </button>
                  <button
                    className="btn-delete"
                    onClick={() => deleteTodo(todo.id)}
                  >
                    删除
                  </button>
                </div>
              </li>
            ))}
          </ul>
          {todos.length === 0 && (
            <div className="empty-state show">
              <p>
                {loading
                  ? '加载中...'
                  : currentFilter === 'all'
                  ? '暂无任务，添加一个开始吧！'
                  : currentFilter === 'active'
                  ? '没有未完成的任务'
                  : '没有已完成的任务'}
              </p>
            </div>
          )}
        </section>

        {/* 底部操作 */}
        <section className="action-section">
          <button
            className="btn-clear-completed"
            onClick={clearCompleted}
            disabled={loading || stats.completed === 0}
          >
            清除已完成 ({stats.completed})
          </button>
          <button
            className="btn-clear-all"
            onClick={clearAll}
            disabled={loading || stats.total === 0}
          >
            清空所有 ({stats.total})
          </button>
        </section>
      </main>
    </div>
  )
}

export default App

