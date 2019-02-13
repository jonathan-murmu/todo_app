from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Todo


class TodoList(ListView):

    model = Todo
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Todo Home'
        return context