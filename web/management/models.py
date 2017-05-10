from django.contrib.auth.models import User
from django.db import models



class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='persona')
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    direccion = models.CharField(blank=True, max_length=500, default='')
    telefono = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno

    class Meta:
        db_table = 'Persona'


