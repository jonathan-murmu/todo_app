from django.contrib import admin

from todo.mixins import ExportCsvMixin
from .models import Todo


class TodoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("title", "description", "task_time", "status", "created_at", "modified_at", "is_active")
    search_fields = (
        'title', 'description'
    )
    list_filter = ('status', 'is_active')
    actions = ["export_as_csv"]


admin.site.register(Todo, TodoAdmin)
