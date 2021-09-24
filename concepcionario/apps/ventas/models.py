from django.db import models
from apps.coches.models import Coches


# Create your models here.

class Ventas(models.Model):
    fecha = models.DateField()
    total = models.IntegerField()
    coche = models.ManyToManyField(Coches)
