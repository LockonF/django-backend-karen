from rest_framework import serializers

from gasolinera.models import Gasolinera, Carga


class GasolineraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasolinera
        fields = '__all__'

class CargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carga
        fields = '__all__'