from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo.models import Todo


class TodoList(ListView):
    """List all the active todos."""

    def get_queryset(self):
        return Todo.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Todo Home'
        context['current'] = 'List'
        return context


class TodoListAPI(TodoList):
    """API for List all the actives todos."""
    def get(self, request):
        response = self.get_queryset()
        return JsonResponse(serializers.serialize('json', response), safe=False)


class TodoDetailView(DetailView):
    """List particular todo."""
    model = Todo

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Todo'
        return context


class TodoDetailAPI(TodoDetailView):
    """API to list particular todo."""

    def get(self, *args,  **kwargs):
        response = self.get_queryset().filter(pk=self.kwargs['pk'])
        return JsonResponse(serializers.serialize('json', response), safe=False)


class TodoCreateView(CreateView):
    """Create a new todo task."""
    model = Todo
    fields = ['title', 'description', 'task_time', 'status']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Todo Task'
        context['current'] = 'Create'
        return context


class TodoUpdate(TodoDetailView, UpdateView):
    """Update an existing todo."""
    model = Todo
    fields = ['title', 'description', 'task_time', 'status']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Todo Task'
        return context


class TodoDelete(DeleteView):
    """Soft delete an existing todo."""
    model = Todo
    success_url = reverse_lazy('todo-list')

    def delete(self, request, *args, **kwargs):
        """Soft Delete.

        Set is_active to False of the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Todo Task'
        return context
