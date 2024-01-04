from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class Proveedor(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
       # help_text='Descripción del proveedor',
        unique=True
    )
    direccion = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    telefono = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    email = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = 'Proveedores'