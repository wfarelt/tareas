from django.urls import path
from django.contrib.auth import views as login
from .views import Home 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', login.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', login.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
]