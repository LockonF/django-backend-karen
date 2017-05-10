from django.db import models

from management.models import Persona
from auto.models import Auto


class Gasolinera(models.Model):
    latitud = models.DecimalField(max_digits=8, decimal_places=5)
    longitud = models.DecimalField(max_digits=8, decimal_places=5)
    ratings_persona = models.ManyToManyField(Persona, through='RatingsGasolinera',
                                     through_fields=('gasolinera', 'persona'))
    class Meta:
        db_table = 'Gasolinera'
        app_label = 'gasolinera'


class Carga(models.Model):
    auto = models.ForeignKey(Auto)
    carga_antes = models.DecimalField(max_digits=6, decimal_places=3)
    carga_despues = models.DecimalField(max_digits=6, decimal_places=3)
    fecha = models.DateTimeField(auto_now_add=True)
    gasolinera = models.ForeignKey(Gasolinera)


    class Meta:
        db_table = 'Carga'
        app_label = 'gasolinera'


class RatingsGasolinera(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    gasolinera = models.ForeignKey(Gasolinera, on_delete=models.CASCADE)
    rating = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'RatingsGasolinera'
        unique_together = ('persona', 'gasolinera')
        app_label = 'gasolinera'