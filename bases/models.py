from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True) # Fecha de Creacion
    fm = models.DateTimeField(auto_now=True) # Fecha de Modificacion
    uc = models.ForeignKey(User, on_delete=models.CASCADE) # Usuario de Creacion
    um = models.IntegerField(blank=True, null=True) # Usuario de Modificacion

    class Meta:
        abstract = True # Para que no cree una tabla en la base de datos