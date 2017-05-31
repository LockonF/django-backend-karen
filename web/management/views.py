from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from management.models import Persona
from management.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):

    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

class PersonaDataView(generics.RetrieveAPIView):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

    def get_object(self):
        return Persona.objects.get(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)