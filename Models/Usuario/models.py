from django.db import models
from Models.Sucursal.models import Sucursal


class TipoUsuario(models.Model):
    idtipo_usuario = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=125)
    password = models.CharField(max_length=45)
    sucursar_id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
