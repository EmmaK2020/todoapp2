from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.addTodoItem, name='add'),
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('completed/<todo_id>', views.completedTodo, name='completed'),
]
