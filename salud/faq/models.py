# En faq/models.py

from django.db import models

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    categorias = models.ManyToManyField('Categoria', related_name='preguntas')

    def __str__(self):
        return self.pregunta

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
