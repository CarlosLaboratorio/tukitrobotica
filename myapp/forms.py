from django import forms
from .models import Productos, Clientes, Vendedores, Comentario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'stock_total', 'imagen']
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
        
        
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedores
        fields = ['nombre', 'apellido', 'email', 'telefono']
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'texto']
        labels = {
            'texto': 'Mensaje',
        }