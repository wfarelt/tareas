from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin as SMM
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.

class ProveedorView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ProveedorNew(SMM, LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'bases:login'
    success_message = 'Proveedor creado exitosamente.'
   
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(SMM, LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'bases:login'
    success_message = 'Proveedor actualizado exitosamente.'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ProveedorDel(SMM, LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'cmp/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('cmp:proveedor_list')
    extra_context = {'clase': 'Proveedor', 'pag_anterior': 'cmp:proveedor_list'}
    login_url = 'bases:login'
    success_message = 'Proveedor eliminado exitosamente.'