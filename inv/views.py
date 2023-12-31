from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, SubCategoria, Marca, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, ProductoForm
from django.urls import reverse_lazy
# Create your views here.

# Categoria

class CategoriaView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CategoriaEdit(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin, DeleteView):
    model = Categoria
    extra_context = {'clase': 'Categoria', 'pag_anterior': 'inv:categoria_list'}
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

# SubCategoria

class SubCategoriaView(LoginRequiredMixin, ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class SubCategoriaNew(LoginRequiredMixin, CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, DeleteView):
    model = SubCategoria
    extra_context = {'clase': 'SubCategoria', 'pag_anterior': 'inv:subcategoria_list'}
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

# Marca
    
class MarcaView(LoginRequiredMixin, ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class MarcaNew(LoginRequiredMixin, CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class MarcaDel(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

class MarcaInactivar(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = 'inv/catalogos_mod.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        object.estado = False
        object.save()
        return redirect('inv:marca_list')
    
# Producto
    
class ProductoView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        form.instance.codigo = form.instance.codigo.upper()
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        form.instance.codigo = form.instance.codigo.upper()
        return super().form_valid(form)

class ProductoInactivar(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'inv/catalogos_mod.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        object.estado = False
        object.save()
        return redirect('inv:producto_list')