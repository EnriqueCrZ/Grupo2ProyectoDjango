from django.forms import ModelForm
from django.forms import  DateInput
from Models.Inscripcion.models import Inscripcion

class formularioInscripcion(ModelForm):


    class Meta:
        model = Inscripcion
        fields = [
            'alumno_id_alumno',
            'nivel_id_nivel',
            'sucursal_id_sucursal',
            'fecha',
        ]

        labels = {
            'alumno_id_alumno': 'Nombre de Alumno',
            'nivel_id_nivel': 'Grado y Nivel',
            'sucursal_id_sucursal': 'Sucursal',
            'fecha':'Fecha de Asignación',
        }
        widgets = {"fecha": DateInput(attrs={'type': 'date'})}