from django.forms import ModelForm
from Models.Alumno.models import Alumno

class formularioNuevoAlumno(ModelForm):

    class Meta:
        model = Alumno
        fields = "__all__"

