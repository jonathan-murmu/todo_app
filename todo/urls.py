from django.urls import path

from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('api/all/', views.TodoListAPI.as_view(), name='todo-list-api'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
    path('api/<int:pk>/', views.TodoDetailAPI.as_view(), name='todo-detail-api'),
    path('add_todo/', views.TodoCreateView.as_view(), name='todo-create'),
    path('edit_todo/<int:pk>/', views.TodoUpdate.as_view(), name='todo-update'),
    path('delete_todo/<int:pk>/', views.TodoDelete.as_view(), name='todo-delete'),
]
