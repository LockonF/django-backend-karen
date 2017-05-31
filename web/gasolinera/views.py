from rest_framework import viewsets, generics

from gasolinera.models import Gasolinera

class GasolineraViewset(viewsets.ModelViewSet):
    serializer_class = GasolineraSerializer
    queryset = Gasolinera.objects.all()