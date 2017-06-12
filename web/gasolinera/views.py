from rest_framework import viewsets, generics

from gasolinera.models import Gasolinera, Carga
from gasolinera.serializers import GasolineraSerializer, CargaSerializer


class GasolineraViewset(viewsets.ModelViewSet):
    serializer_class = GasolineraSerializer
    queryset = Gasolinera.objects.all()

class CargaViewSet(viewsets.ModelViewSet):
    serializer_class = CargaSerializer
    queryset = Carga.objects.all()