from django.db import models


class TipoUsuario(models.Model):
    idtipo_usuario = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    correo = models.EmailField(max_length=125)
    password = models.CharField(max_length=45)
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
