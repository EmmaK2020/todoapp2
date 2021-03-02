from django.shortcuts import render
from . forms import TodoListForm
from . models import Todolist
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

@require_POST  #decorator
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text']) #Todolist is MODEL/DB 
        new_todo.save()
    return redirect('index') #will call index again and send todo_items ordered by ID

def index (request):
    todo_items = Todolist.objects.order_by ('id')
    form = TodoListForm() #instance of form class created 
    context = {'todo_items' : todo_items, 'form':form}
    return render (request, 'todolist/index.html', context)

def deleteCompleted(request):
    Todolist.objects.filter(completed=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')

def completedTodo(request, todo_id): #receiving arguemnt when function called 
    todo = Todolist.objects.get(pk=todo_id)#todo VARIABLE = item from MODEL Todolist whose PK is equal to received argument
    todo.completed = True
    todo.save()
    return redirect('index')


  


