from django.urls import path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorDel

urlpatterns = [
    # Proveedores
    path('proveedores/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/delete/<int:pk>', ProveedorDel.as_view(), name='proveedor_delete'),
]