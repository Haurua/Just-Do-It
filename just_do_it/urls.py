from django.urls import path
from .views import Index, CreateTask, TaskDetail, DeleteTask, UpdateTask

urlpatterns = [
    path('', Index.as_view(), name='just-do-it'),
    path('create-task', CreateTask.as_view(), name='just-do-it-create'),
    path('<pk>/details', TaskDetail.as_view(), name='just-do-it-detail'),
    path('<pk>/revise', UpdateTask.as_view(), name='just-do-it-update'),
    path('<pk>/delete', DeleteTask.as_view(), name='just-do-it-delete'),
]