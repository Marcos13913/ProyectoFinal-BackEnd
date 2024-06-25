from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    fecha = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.fecha}'