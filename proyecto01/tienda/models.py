
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    SKU = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.SKU}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.duracion}"