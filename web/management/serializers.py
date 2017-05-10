from rest_framework import serializers

from auto.serializers import AutoSerializer
from management.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    auto = AutoSerializer
    class Meta:
        model = Persona
        fields = ('user', 'nombre', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'foto', 'auto')