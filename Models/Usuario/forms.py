from django.forms import ModelForm
from Models.Usuario.models import TipoUsuario, Usuario


class formularioUsuario(ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"

class formularioTipoUsuario(ModelForm):

    class Meta:
        model = TipoUsuario
        fields = "__all__"