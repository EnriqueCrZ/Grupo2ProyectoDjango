from django.db import models


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=45)
    direccion = models.CharField(max_length=125)
    correo = models.CharField(max_length=125)
    telefono = models.CharField(max_length=10)