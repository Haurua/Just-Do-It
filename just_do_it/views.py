from django.shortcuts import render, redirect
from django.views import View
from .models import JustDoItTasks
from .forms import JustDoItForm


class Index(View):
    def get(self, request, *args, **kwargs):
        query_set = JustDoItTasks.objects.all()
        context = {"data": query_set}
        return render(request, 'just_do_it/list_view.html', context=context)


class CreateTask(View):
    def get(self, request, *args, **kwargs):
        form = JustDoItForm()
        context = {"form": form}
        return render(request, 'just_do_it/create_task.html', context)

    def post(self, request, *args, **kwargs):
        form = JustDoItForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('just-do-it')


class TaskDetail(View):
    def get(self, request, pk, *args, **kwargs):
        query_obj = JustDoItTasks.objects.get(pk=pk)
        context = {'data': query_obj}
        return render(request, 'just_do_it/task_detail.html', context)


class UpdateTask(View):
    def get(self, request, pk, *args, **kwargs):
        template = 'to_do_list/update_task.html'
        obj = JustDoItTasks.objects.get(pk=pk)
        obj_completed = JustDoItTasks.objects.values_list('completed', flat=True).get(pk=pk)
        form = JustDoItForm(instance=obj)
        context = {
            "form": form,
            "completed": obj_completed
        }
        return render(request, 'just_do_it/update_task.html', context)

    def post(self, request, pk, *args, **kwargs):
        obj = JustDoItTasks.objects.get(pk=pk)
        form = JustDoItForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('just-do-it-detail', pk)


class DeleteTask(View):
    def post(self, request, pk, *args, **kwargs):
        obj = JustDoItTasks.objects.get(pk=pk)
        obj.delete()
        return redirect('just-do-it')
