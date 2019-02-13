from django.urls import path

from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
    path('add_todo/', views.TodoCreateView.as_view(), name='todo-create'),
    path('edit_todo/<int:pk>/', views.TodoUpdate.as_view(), name='todo-update'),
    path('delete_todo/<int:pk>/', views.TodoDelete.as_view(), name='todo-delete'),
]
