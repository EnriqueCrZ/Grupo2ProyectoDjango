from django.db import models


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    dpi = models.CharField(max_length=13, unique=True)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=125)
<<<<<<< HEAD
=======

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
<<<<<<< HEAD
=======

>>>>>>> 20a72d395c09def9a8acb9a816eb1404e86847d7
>>>>>>> 16b887b38d6f776fa4893fc39913c906d5530ed4
