from django.forms import ModelForm
from Models.Nivel.models import Nivel, Grado


class formularioNivel(ModelForm):

    class Meta:
        model = Nivel
        fields = "__all__"

class formularioGrado(ModelForm):

    class Meta:
        model = Grado
        fields = "__all__"
