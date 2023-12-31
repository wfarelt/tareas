from django import forms
from .models import Categoria, SubCategoria, Marca, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la categoria', 'estado':'Estado'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la subcategoria', 'estado':'Estado'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['categoria'].empty_label = 'Seleccione Categoria'
        self.fields['categoria'].widget.attrs['class'] = 'form-control select2'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
            
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la marca', 'estado':'Estado'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'

class ProductoForm(forms.ModelForm):
    subcategoria = forms.ModelChoiceField(
        queryset=SubCategoria.objects.filter(estado=True).order_by('descripcion')
    )
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barra', 'descripcion', 'estado', 'precio', 'existencia', 'ultima_compra', 'marca', 'subcategoria']
        exclude = ['usuario_modificacion', 'fecha_modificacion']
        labels = {'descripcion':'Descripcion del producto', 'estado':'Estado', 'precio':'Precio', 'existencia':'Existencia', 'ultima_compra':'Ultima Compra', 'marca':'Marca', 'subcategoria':'Subcategoria'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['codigo'].widget.attrs['autofocus'] = True
        self.fields['codigo'].widget.attrs['class'] = 'form-control'
        self.fields['codigo_barra'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['precio'].widget.attrs['class'] = 'form-control'
        self.fields['existencia'].widget.attrs['class'] = 'form-control'
        self.fields['ultima_compra'].widget.attrs['class'] = 'form-control'
        self.fields['marca'].widget.attrs['class'] = 'form-control'
        self.fields['subcategoria'].widget.attrs['class'] = 'form-control'