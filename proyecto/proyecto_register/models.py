from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Csv(models.Model):
    csv = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

