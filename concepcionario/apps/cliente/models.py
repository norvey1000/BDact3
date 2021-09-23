from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=15)
