from rest_framework import serializers

from auto.models import MarcaAuto, ModeloAuto, Auto


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'

class ModeloAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloAuto
        fields = '__all__'

class MarcaAutoSerializer(serializers.ModelSerializer):
    modelos = ModeloAutoSerializer(many=True, read_only=True)
    class Meta:
        model = MarcaAuto
        fields = ('id', 'nombre', 'logo', 'modelos')