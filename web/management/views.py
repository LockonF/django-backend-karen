from rest_framework import viewsets, generics
from rest_framework.response import Response

from management.models import Persona
from management.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):

    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

class PersonaDataView(generics.RetrieveAPIView):
    serializer_class = PersonaSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return Persona.objects.get(user=user)