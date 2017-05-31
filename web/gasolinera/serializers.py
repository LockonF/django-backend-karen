from rest_framework import serializers

from gasolinera.models import Gasolinerado

class GasolineraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasolinera
        fields = '__all__'
