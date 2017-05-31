from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from auto.serializers import AutoSerializer
from management.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    auto = AutoSerializer
    class Meta:
        model = Persona
        fields = ('user', 'nombre', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'foto', 'auto')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ('password', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User()
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)