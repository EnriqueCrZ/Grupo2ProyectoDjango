from django.db import models


class Grado(models.Model):
    id_grado = models.AutoField(primary_key=True)
    nombre_grado = models.CharField(max_length=45)

    def __str__(self):
        return '{}'.format(self.nombre_grado)

class Nivel(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nombre_nivel = models.CharField(max_length=45)
    grado_id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.grado_id_grado,self.nombre_nivel)