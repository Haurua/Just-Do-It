import uuid
from django.db import models
from django.contrib.auth.models import User


class JustDoItTasks(models.Model):
    """
    Model containing fields pertaining to the To-Do items.
    """
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
