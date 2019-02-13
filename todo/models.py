from django.db import models


class Todo(models.Model):
    """Model for todo app."""
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = (
        (1, PENDING),
        (2, IN_PROGRESS),
        (3, COMPLETED),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    task_time = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
