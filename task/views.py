from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms


# Create your views here.

def task_list(request):
    tasks = models.Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = forms.TaskForm()
    return render(request, 'task/task_create.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = forms.TaskForm(instance=task)
    return render(request, 'task/task_edit.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.delete()
    return redirect('task:task_list')