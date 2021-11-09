const todos = document.querySelector('.todo-list')

const todoList = new Sortable(todos, {
	animation: 120
})