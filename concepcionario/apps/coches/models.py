from django.db import models

# Create your models here.

class Coches(models.Model):
    matricula = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.IntegerField(max_length=20)
    precio = models.DecimalField(max_length=20)
