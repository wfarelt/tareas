from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskModal(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/task_modal.html'
    context_object_name = 'tasks'
    form_class = TaskForm
    success_url = reverse_lazy('task:task_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.title = form.instance.title.upper()
        return super().form_valid(form)



class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('task:task_list')
    login_url = 'bases:login'
    ordering = ['complete']

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/task_modal.html'
    context_object_name = 'tasks'
    form_class = TaskForm
    success_url = reverse_lazy('task:task_list')
    login_url = 'bases:login'

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.title = form.instance.title.upper()
        return super().form_valid(form)

class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_modal.html'
    context_object_name = 'tasks'
    form_class = TaskForm
    success_url = reverse_lazy('task:task_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.title = form.instance.title.upper()
        return super().form_valid(form) 

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('task:task_list')
    login_url = 'bases:login'

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task:task_detail', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_create.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_edit.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task:task_list')

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = True
    task.save()
    return redirect('task:task_list')
    