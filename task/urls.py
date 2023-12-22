from django.urls import path
from .views import task_list, task_detail, task_create, task_edit, task_delete
urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('create/', task_create, name='task_create'),
    path('<int:pk>/edit/', task_edit, name='task_edit'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
]

