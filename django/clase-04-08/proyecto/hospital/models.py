from django.db import models

# Create your models here.


class HospitalMedico(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    antiguedad = models.IntegerField()

    def __str__(self):
        return self.nombre