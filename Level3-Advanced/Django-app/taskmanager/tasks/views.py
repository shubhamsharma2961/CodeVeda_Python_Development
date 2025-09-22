from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task
from .forms import SignUpForm, TaskForm


class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        qs = Task.objects.filter(owner=self.request.user)
        if self.request.user.is_staff:
            qs = Task.objects.all()
        return qs   
    
class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')   

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TaskOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        return self.request.user.is_staff or task.owner == self.request.user

class TaskDetailView(LoginRequiredMixin, TaskOwnerMixin, generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskUpdateView(LoginRequiredMixin, TaskOwnerMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(LoginRequiredMixin, TaskOwnerMixin, generic.DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')
