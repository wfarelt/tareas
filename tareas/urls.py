from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include (('bases.urls','bases'), namespace='bases')),
    path('task/', include('task.urls'), name='task'),
    path('inv/', include(('inv.urls','inv'), namespace='inv')),
    
]
