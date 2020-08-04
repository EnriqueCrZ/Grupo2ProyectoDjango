from django.db import models


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=45)
    direccion = models.CharField(max_length=125)
    correo = models.EmailField(max_length=125)
    telefono = models.CharField(max_length=10)

<<<<<<< HEAD
=======
<<<<<<< HEAD
    def __str__(self):
        return self.nombre
=======
    #def __str__(self):
     #  return '{}'.format(self.nombre)

>>>>>>> 16b887b38d6f776fa4893fc39913c906d5530ed4
    def __str__(self):
        return self.nombre
    #def __str__(self):
     #  return '{}'.format(self.nombre)

>>>>>>> 20a72d395c09def9a8acb9a816eb1404e86847d7
