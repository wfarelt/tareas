from django.urls import path
from .views import *

app_name = 'task'

urlpatterns = [
    path('list/', TaskView.as_view(), name='task_list'),
    #path('list/', task_list, name='task_list'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    #path('create/', task_create, name='task_create'),
    path('<int:pk>/edit/', TaskEdit.as_view(), name='task_edit'),
    #path('<int:pk>/edit/', task_edit, name='task_edit'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    #path('<int:pk>/delete/', task_delete, name='task_delete'),
    path('<int:pk>/complete/', task_complete, name='task_complete'),
    path('modal/', TaskModal.as_view(), name='task_modal'),
]

