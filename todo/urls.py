from django.urls import path

from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),

]
