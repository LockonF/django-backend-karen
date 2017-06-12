from django.conf.urls import url

import docker_django.router as baseRouter
from gasolinera.views import GasolineraViewset, CargaViewSet

baseRouter.router.register(r'gasolinera', GasolineraViewset, 'gasolinera')
baseRouter.router.register(r'carga', CargaViewSet, 'carga')



urlpatterns = [
#    url(r'^marca-auto/(?P<pk>[0-9])/modelo-auto$', ModelosByMarcaView.as_view()),
]
