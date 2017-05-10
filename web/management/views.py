from rest_framework import viewsets

from management.models import Persona
from management.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):

    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
