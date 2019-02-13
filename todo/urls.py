from django.urls import path

from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
]
