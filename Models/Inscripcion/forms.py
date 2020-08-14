from django.forms import ModelForm
from django.forms import DateInput
from Models.Inscripcion.models import Inscripcion, Nota

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
        widgets = {

            #"alumno_id_alumno": TextInput(),
            #"alumno_id_alumno":  autocomplete.ModelSelect2(url='inscribir'),
            "fecha": DateInput(attrs={'type': 'date'}),
                   }
class formularioNota(ModelForm):


    class Meta:
        model = Nota
        fields = [
            'inscripcion_id_inscripcion',
            'nota',
            'fecha',
        ]

        labels = {
            'inscripcion_id_inscripcion': 'Alumno',
            'nota': 'Nota',
            'fecha': 'Fecha',
        }
        widgets = {

            # "alumno_id_alumno": TextInput(),
            # "alumno_id_alumno":  autocomplete.ModelSelect2(url='inscribir'),
            "fecha": DateInput(attrs={'type': 'date'}),
        }

