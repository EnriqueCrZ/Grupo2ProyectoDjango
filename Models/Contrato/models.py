from django.db import models
from Models.Nivel.models import Nivel


class Catedratico(models.Model):
    id_catedratico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    dpi = models.CharField(max_length=13, unique=True)
    telefono = models.CharField(max_length=10)
<<<<<<< HEAD
    correo = models.EmailField(max_length=125)
=======
    correo = models.CharField(max_length=125)
>>>>>>> 859b207c7031340d22030ab0c290d1650ffa6675


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha = models.DateField()
    catedratico_id_catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    nivel_id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)