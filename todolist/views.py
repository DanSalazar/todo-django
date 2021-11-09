from django.shortcuts import render,redirect
from .models import TodoList

def index(request):
	todos = TodoList.objects.all()
	if request.method == 'POST':
		if 'addTodo' in request.POST:
			todo_title = request.POST['todo-name']
			todo = TodoList(title=todo_title)
			todo.save()
			return redirect('/')
	if 'deleteTodo' in request.POST:
		todo_search = request.POST['deleteTodo']
		todo_to_delete = TodoList.objects.filter(title=todo_search)  
		todo_to_delete.delete()
		return redirect('/')

	return render(request, 'home.html', { 'todos': todos })
   