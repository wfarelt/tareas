from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #para que solo los usuarios logueados puedan ver la pagina
from django.views.generic import TemplateView
# Create your views here.


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'
    