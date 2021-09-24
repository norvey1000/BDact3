from django.db import models

# Create your models here.
class Marca(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=400)
    