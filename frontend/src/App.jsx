import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const API_BASE = '/api'

function App() {
  const [todos, setTodos] = useState([])
  const [inputValue, setInputValue] = useState('')
  const [currentFilter, setCurrentFilter] = useState('all')
  const [loading, setLoading] = useState(false)
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1)
  const [pageSize, setPageSize] = useState(10)
  const [totalPages, setTotalPages] = useState(1)
  const [total, setTotal] = useState(0)
  
  // Search state
  const [searchQuery, setSearchQuery] = useState('')
  const [searchType, setSearchType] = useState('fuzzy') // 'fuzzy' or 'exact'
  const [activeSearch, setActiveSearch] = useState('')
  
  // Edit state
  const [editingId, setEditingId] = useState(null)
  const [editValue, setEditValue] = useState('')
  
  // Stats
  const [stats, setStats] = useState({ total: 0, active: 0, completed: 0 })

  // Fetch todos with search and pagination
  const fetchTodos = async () => {
    try {
      setLoading(true)
      const params = {
        filter: currentFilter,
        page: currentPage,
        page_size: pageSize
      }
      
      if (activeSearch) {
        params.search = activeSearch
        params.search_type = searchType
      }
      
      const response = await axios.get(`${API_BASE}/todos`, { params })
      setTodos(response.data.todos || [])
      setTotal(response.data.total || 0)
      setTotalPages(response.data.total_pages || 1)
      setCurrentPage(response.data.page || 1)
      
      // Fetch stats
      const statsResponse = await axios.get(`${API_BASE}/stats`)
      setStats(statsResponse.data)
    } catch (error) {
      console.error('Failed to fetch todos:', error)
      alert('❌ Failed to load data, please check if backend service is running')
    } finally {
      setLoading(false)
    }
  }

  // Fetch on mount and when filters change
  useEffect(() => {
    fetchTodos()
  }, [currentFilter, currentPage, pageSize, activeSearch, searchType])

  // Handle search
  const handleSearch = (e) => {
    e.preventDefault()
    setActiveSearch(searchQuery)
    setCurrentPage(1) // Reset to first page when searching
  }

  // Clear search
  const clearSearch = () => {
    setSearchQuery('')
    setActiveSearch('')
    setCurrentPage(1)
  }

  // Add todo
  const handleAddTodo = async (e) => {
    e.preventDefault()
    const text = inputValue.trim()

    if (text === '') {
      alert('⚠️ Please enter task content!')
      return
    }

    try {
      await axios.post(`${API_BASE}/todos`, { text })
      setInputValue('')
      fetchTodos()
      alert('✅ Task added successfully!')
    } catch (error) {
      console.error('Add failed:', error)
      alert('❌ Failed to add, please try again')
    }
  }

  // Toggle todo completion
  const toggleTodo = async (id, currentCompleted) => {
    try {
      await axios.put(`${API_BASE}/todos/${id}`, {
        completed: !currentCompleted
      })
      fetchTodos()
    } catch (error) {
      console.error('Update failed:', error)
      alert('❌ Update failed, please try again')
    }
  }

  // Start editing
  const startEdit = (todo) => {
    setEditingId(todo.id)
    setEditValue(todo.text)
  }

  // Save edit
  const saveEdit = async (id) => {
    const text = editValue.trim()
    if (text === '') {
      alert('⚠️ Task name cannot be empty!')
      return
    }

    try {
      await axios.put(`${API_BASE}/todos/${id}`, { text })
      setEditingId(null)
      setEditValue('')
      fetchTodos()
      alert('✅ Task updated successfully!')
    } catch (error) {
      console.error('Update failed:', error)
      alert('❌ Update failed, please try again')
    }
  }

  // Cancel edit
  const cancelEdit = () => {
    setEditingId(null)
    setEditValue('')
  }

  // Delete todo
  const handleDeleteTodo = async (id) => {
    if (!confirm('⚠️ Are you sure you want to delete this task?\nThis cannot be undone!')) return
    try {
      await axios.delete(`${API_BASE}/todos/${id}`)
      fetchTodos()
      alert('✅ Task deleted')
    } catch (error) {
      console.error('Delete failed:', error)
      alert('❌ Delete failed, please try again')
    }
  }

  // Clear completed
  const handleClearCompleted = async () => {
    if (stats.completed === 0) {
      alert('ℹ️ No completed tasks to clear')
      return
    }
    if (!confirm('⚠️ Are you sure you want to clear all completed tasks?\nThis cannot be undone!')) return
    try {
      await axios.delete(`${API_BASE}/todos/clear/completed`)
      fetchTodos()
      alert('✅ Completed tasks cleared')
    } catch (error) {
      console.error('Clear failed:', error)
      alert('❌ Clear failed, please try again')
    }
  }

  // Clear all
  const handleClearAll = async () => {
    if (stats.total === 0) {
      alert('ℹ️ No tasks to clear')
      return
    }
    if (!confirm('⚠️ Warning! Are you sure you want to clear all tasks?\nThis cannot be undone!')) return
    try {
      await axios.delete(`${API_BASE}/todos/clear/all`)
      fetchTodos()
      alert('✅ All tasks cleared')
    } catch (error) {
      console.error('Clear all failed:', error)
      alert('❌ Clear failed, please try again')
    }
  }

  // Pagination controls
  const goToPage = (page) => {
    if (page >= 1 && page <= totalPages) {
      setCurrentPage(page)
    }
  }

  return (
    <div className="container">
      {/* Animated background particles */}
      <div className="particles"></div>
      
      <header>
        <h1>✨ Advanced Todo Manager</h1>
        <p className="subtitle">Organize your tasks with powerful search & filters</p>
      </header>

      <main>
        {/* Search Section - Top */}
        <section className="search-section">
          <form onSubmit={handleSearch} className="search-form">
            <div className="search-input-group">
              <input
                type="text"
                placeholder="🔍 Search tasks..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="search-input"
              />
              <div className="search-type-toggle">
                <button
                  type="button"
                  className={`toggle-btn ${searchType === 'fuzzy' ? 'active' : ''}`}
                  onClick={() => setSearchType('fuzzy')}
                >
                  Fuzzy
                </button>
                <button
                  type="button"
                  className={`toggle-btn ${searchType === 'exact' ? 'active' : ''}`}
                  onClick={() => setSearchType('exact')}
                >
                  Exact
                </button>
              </div>
            </div>
            <button type="submit" className="btn-search">
              Search
            </button>
            {activeSearch && (
              <button type="button" className="btn-clear-search" onClick={clearSearch}>
                Clear
              </button>
            )}
          </form>
          {activeSearch && (
            <div className="search-info">
              Searching for "{activeSearch}" ({searchType}) - Found {total} result(s)
            </div>
          )}
        </section>

        {/* Add Task Section */}
        <section className="add-section">
          <form onSubmit={handleAddTodo} autoComplete="off">
            <input
              type="text"
              id="new-todo"
              placeholder="➕ Add a new task..."
              required
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              disabled={loading}
              aria-label="New task input"
              title="Enter task content"
            />
            <button type="submit" className="btn-add" disabled={loading}>
              <span>Add Task</span>
              <span className="add-icon">+</span>
            </button>
          </form>
        </section>

        {/* Stats and Filter Section */}
        <section className="control-section">
          <div className="task-stats">
            <div className="stat-item">
              <span className="stat-label">Total:</span>
              <strong className="stat-value">{stats.total}</strong>
            </div>
            <div className="stat-item">
              <span className="stat-label">Active:</span>
              <strong className="stat-value active">{stats.active}</strong>
            </div>
            <div className="stat-item">
              <span className="stat-label">Completed:</span>
              <strong className="stat-value completed">{stats.completed}</strong>
            </div>
          </div>
          <div className="filter-buttons">
            <button
              className={`filter-btn ${currentFilter === 'all' ? 'active' : ''}`}
              onClick={() => { setCurrentFilter('all'); setCurrentPage(1); }}
              disabled={loading}
            >
              All
            </button>
            <button
              className={`filter-btn ${currentFilter === 'active' ? 'active' : ''}`}
              onClick={() => { setCurrentFilter('active'); setCurrentPage(1); }}
              disabled={loading}
            >
              Active
            </button>
            <button
              className={`filter-btn ${currentFilter === 'completed' ? 'active' : ''}`}
              onClick={() => { setCurrentFilter('completed'); setCurrentPage(1); }}
              disabled={loading}
            >
              Completed
            </button>
          </div>
        </section>

        {/* Task List Section */}
        <section className="list-section">
          {loading ? (
            <div className="loading-state">
              <div className="spinner"></div>
              <p>Loading...</p>
            </div>
          ) : (
            <>
              <ul id="todo-list">
                {todos.length === 0 && (
                  <div className="empty-state show">
                    <div className="empty-icon">📋</div>
                    <p>{activeSearch ? 'No tasks found matching your search' : 'No tasks yet, add one to get started!'}</p>
                  </div>
                )}
                {todos.map(todo => (
                  <li key={todo.id} className={`todo-item ${todo.completed ? 'completed' : ''}`}>
                    <div 
                      className="todo-checkbox" 
                      onClick={() => toggleTodo(todo.id, todo.completed)}
                      title={todo.completed ? 'Mark as incomplete' : 'Mark as complete'}
                    ></div>
                    
                    {editingId === todo.id ? (
                      <div className="edit-mode">
                        <input
                          type="text"
                          value={editValue}
                          onChange={(e) => setEditValue(e.target.value)}
                          className="edit-input"
                          autoFocus
                          onKeyPress={(e) => {
                            if (e.key === 'Enter') saveEdit(todo.id)
                            if (e.key === 'Escape') cancelEdit()
                          }}
                        />
                        <button className="btn-save" onClick={() => saveEdit(todo.id)}>
                          ✓ Save
                        </button>
                        <button className="btn-cancel" onClick={cancelEdit}>
                          ✕ Cancel
                        </button>
                      </div>
                    ) : (
                      <>
                        <span 
                          className="todo-text" 
                          onDoubleClick={() => !todo.completed && startEdit(todo)}
                          title="Double-click to edit"
                        >
                          {todo.text}
                        </span>
                        <div className="todo-actions">
                          {!todo.completed && (
                            <button
                              className="btn-edit"
                              onClick={() => startEdit(todo)}
                              title="Edit task"
                            >
                              ✏️ Edit
                            </button>
                          )}
                          <button
                            className="btn-complete"
                            onClick={() => toggleTodo(todo.id, todo.completed)}
                          >
                            {todo.completed ? '↶ Undo' : '✓ Complete'}
                          </button>
                          <button
                            className="btn-delete"
                            onClick={() => handleDeleteTodo(todo.id)}
                          >
                            🗑️ Delete
                          </button>
                        </div>
                      </>
                    )}
                  </li>
                ))}
              </ul>

              {/* Pagination */}
              {totalPages > 1 && (
                <div className="pagination">
                  <button
                    className="page-btn"
                    onClick={() => goToPage(1)}
                    disabled={currentPage === 1}
                  >
                    « First
                  </button>
                  <button
                    className="page-btn"
                    onClick={() => goToPage(currentPage - 1)}
                    disabled={currentPage === 1}
                  >
                    ‹ Prev
                  </button>
                  
                  <div className="page-numbers">
                    {[...Array(totalPages)].map((_, i) => {
                      const page = i + 1
                      // Show current page and 2 pages before/after
                      if (
                        page === 1 ||
                        page === totalPages ||
                        (page >= currentPage - 2 && page <= currentPage + 2)
                      ) {
                        return (
                          <button
                            key={page}
                            className={`page-number ${page === currentPage ? 'active' : ''}`}
                            onClick={() => goToPage(page)}
                          >
                            {page}
                          </button>
                        )
                      } else if (page === currentPage - 3 || page === currentPage + 3) {
                        return <span key={page} className="page-ellipsis">...</span>
                      }
                      return null
                    })}
                  </div>

                  <button
                    className="page-btn"
                    onClick={() => goToPage(currentPage + 1)}
                    disabled={currentPage === totalPages}
                  >
                    Next ›
                  </button>
                  <button
                    className="page-btn"
                    onClick={() => goToPage(totalPages)}
                    disabled={currentPage === totalPages}
                  >
                    Last »
                  </button>
                  
                  <div className="page-info">
                    Page {currentPage} of {totalPages} ({total} total tasks)
                  </div>
                  
                  <select 
                    className="page-size-select"
                    value={pageSize}
                    onChange={(e) => { setPageSize(Number(e.target.value)); setCurrentPage(1); }}
                  >
                    <option value={5}>5 per page</option>
                    <option value={10}>10 per page</option>
                    <option value={20}>20 per page</option>
                    <option value={50}>50 per page</option>
                  </select>
                </div>
              )}
            </>
          )}
        </section>

        {/* Bottom Actions */}
        <section className="action-section">
          <button
            className="btn-clear-completed"
            onClick={handleClearCompleted}
            disabled={loading || stats.completed === 0}
          >
            🧹 Clear Completed ({stats.completed})
          </button>
          <button
            className="btn-clear-all"
            onClick={handleClearAll}
            disabled={loading || stats.total === 0}
          >
            🗑️ Clear All ({stats.total})
          </button>
        </section>
      </main>

      <footer className="app-footer">
        <p>Made with ❤️ using React + FastAPI</p>
      </footer>
    </div>
  )
}

export default App
