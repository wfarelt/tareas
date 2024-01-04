from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['descripcion','direccion','telefono','email']
        labels = {'descripcion':'Descripcion del Proveedor','direccion':'Direccion','telefono':'Telefono','email':'Correo Electronico'}
        widget = {'descripcion':forms.TextInput(),'direccion':forms.TextInput(),'telefono':forms.TextInput(),'email':forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            #print(field)
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    
    # validar que no se repita la descripcion del proveedor
    def clean(self):
        try:
            sc = Proveedor.objects.get(descripcion=self.cleaned_data['descripcion'].upper())
            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError('Registro ya existe')
            elif self.instance.pk != sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError('Cambio no permitido')
        except Proveedor.DoesNotExist:
            pass
        return self.cleaned_data
    

    
    
