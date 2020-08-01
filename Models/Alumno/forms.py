from django.forms import ModelForm
from Models.Alumno.models import Alumno

class formularioNuevoAlumno(ModelForm):

    class Meta:
        model = Alumno
        fields = [
            'nombre',
            'apellido',
            'dpi',
            'telefono',
            'correo',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dpi': 'DPI',
            'telefono': 'Telefono O Celular',
            'correo': 'Correo electronico',
        }


