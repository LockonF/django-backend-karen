from rest_framework import viewsets, generics

from auto.models import MarcaAuto, ModeloAuto, Auto
from auto.serializers import MarcaAutoSerializer, ModeloAutoSerializer, AutoSerializer


class MarcaAutoViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaAutoSerializer
    queryset = MarcaAuto.objects.all()

class ModeloAutoViewSet(viewsets.ModelViewSet):
    serializer_class = ModeloAutoSerializer
    queryset = ModeloAuto.objects.all()

class ModelosByMarcaView(generics.ListAPIView):
    lookup_url_kwarg = 'pk'
    serializer_class = ModeloAutoSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return ModeloAuto.objects.filter(marca=pk)

class AutoViewSet(viewsets.ModelViewSet):
    serializer_class = AutoSerializer
    queryset = Auto.objects.all()