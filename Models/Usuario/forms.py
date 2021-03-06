from django import forms
from Models.Usuario.models import TipoUsuario, User
from Models.Sucursal.models import Sucursal
from django.contrib.auth import get_user_model

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')

    class Meta:
        model = get_user_model()
        fields = ('correo', 'nombre', 'password', 'sucursal_id_sucursal', 'tipo_usuario_idtipo_usuario')
        labels = {
            'sucursal_id_sucursal': 'Sucursal',
            'tipo_usuario_idtipo_usuario': 'Rol',
        }


class LoginForm(forms.Form):
    correo = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password', 'correo', 'nombre')
