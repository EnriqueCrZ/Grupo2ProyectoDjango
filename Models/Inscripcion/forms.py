from django.forms import forms
from django.forms import ModelForm
from Models.Inscripcion.models import Inscripcion, Nota



class formularioInscripcion(ModelForm):
    class Meta:
        model = Inscripcion
        fields = "__all__"
        widgets = {"fecha_registro": forms.DateInput(attrs={'type': 'date'})}


class formularioNotas(ModelForm):
    class Meta:
        model = Nota
        fields = "__all__"
        widgets = {"fecha_notas": forms.DateInput(attrs={'type': 'date'})}


