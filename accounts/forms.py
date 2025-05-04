from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class PerfilForm(forms.ModelForm):
    cumpleaños = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Perfil
        fields = ['avatar', 'cumpleaños']
        
class EditarUsuarioForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("new_password1")
        p2 = cleaned_data.get("new_password2")
        if p1 or p2:
            if p1 != p2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data