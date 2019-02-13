from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todo.models import Todo


class TodoList(ListView):
    paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        return Todo.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Todo Home'
        return context


class TodoDetailView(DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Todo'
        return context


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'task_time', 'status']


class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'task_time', 'status']
    template_name_suffix = '_update_form'


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)
