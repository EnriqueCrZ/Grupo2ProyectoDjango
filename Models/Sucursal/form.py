from django.forms import ModelForm
from Models.Sucursal.models import Sucursal


class formularioSucursal(ModelForm):

    class Meta:
        model = Sucursal
        fields = "__all__"