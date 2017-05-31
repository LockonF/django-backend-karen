from rest_framework import serializers

from auto.serializers import AutoSerializer
from management.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    auto = AutoSerializer
    class Meta:
        model = Persona
        fields = '__all__'