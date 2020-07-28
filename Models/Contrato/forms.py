from django.forms import ModelForm
from Models.Contrato.models import Contrato
from Models.Contrato.models import Catedratico

class formularioNuevoCatedratico(ModelForm):

    class Meta:
        model = Catedratico
        fields = "__all__"

class formularioContrato(ModelForm):

    class Meta:
        model = Contrato
        fields = "__all__"




