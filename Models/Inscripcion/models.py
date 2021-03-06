from django.db import models
from Models.Alumno.models import Alumno
from Models.Nivel.models import Nivel
from Models.Sucursal.models import Sucursal
from Models.Usuario.models import User


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    alumno_id_alumno = models.ForeignKey(Alumno, blank=False, on_delete=models.CASCADE)
    nivel_id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    sucursal_id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField()
    usuario_id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.alumno_id_alumno)

class Nota(models.Model):
    id_nota = models.AutoField(primary_key=True)
    fecha = models.DateField()
    nota = models.IntegerField()
    inscripcion_id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
