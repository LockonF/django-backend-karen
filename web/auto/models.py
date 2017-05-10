from django.db import models
from django.contrib.auth.models import User

from management.models import Persona


class MarcaAuto(models.Model):
    nombre = models.TextField(max_length=200)
    logo = models.ImageField(upload_to='marcas_auto')

    class Meta:
        db_table = 'MarcaAuto'
    def __str__(self):
        return self.nombre

class ModeloAuto(models.Model):
    nombre = models.TextField(max_length=200)
    marca = models.ForeignKey(MarcaAuto, related_name="modelos")

    class Meta:
        db_table = 'ModeloAuto'
    def __str__(self):
        return self.nombre

class Auto(models.Model):
    protocolo = models.IntegerField()
    modelo = models.ForeignKey(ModeloAuto)
    year = models.IntegerField()
    persona = models.ForeignKey(Persona, related_name="auto")
    motor = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        db_table = 'Auto'