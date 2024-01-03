from django.contrib import admin
from .models import Categoria, Marca, SubCategoria, Producto

from import_export.admin import ImportExportModelAdmin
# Register your models here.



admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Marca)

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    pass
