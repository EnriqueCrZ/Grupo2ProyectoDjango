from django.db import models


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=45)
    direccion = models.CharField(max_length=125)
<<<<<<< HEAD
    correo = models.EmailField(max_length=125)
=======
    correo = models.CharField(max_length=125)
>>>>>>> 859b207c7031340d22030ab0c290d1650ffa6675
    telefono = models.CharField(max_length=10)