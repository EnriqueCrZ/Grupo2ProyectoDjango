from django.forms import ModelForm, DateInput
from Models.Contrato.models import Contrato
from Models.Contrato.models import Catedratico

class formioNuevoCatedratico(ModelForm):

    class Meta:
        model = Catedratico
        fields = "__all__"

class formContrato(ModelForm):

    class Meta:
        model = Contrato
        fields = [

            'catedratico_id_catedratico',
            'nivel_id_nivel',
            'fecha'
        ]

        labels = {
            'fecha': 'Fecha',
            'catedratico_id_catedratico': 'Nombre del Catedratico',
            'nivel_id_nivel': 'Grado y Seccion',

        }
        widgets = {

            # "alumno_id_alumno": TextInput(),
            # "alumno_id_alumno":  autocomplete.ModelSelect2(url='inscribir'),
            "fecha": DateInput(attrs={'type': 'date'}),
        }




