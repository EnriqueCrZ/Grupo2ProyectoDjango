from django.db import models


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    dpi = models.CharField(max_length=13, unique=True)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=125)

    def __str__(self):
        return self.id_alumno
