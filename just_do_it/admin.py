from django.contrib import admin
from .models import JustDoItTasks


@admin.register(JustDoItTasks)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "completed",
        "created"
    ]
