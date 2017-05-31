from django.conf.urls import url

from gasolinera.views import GasolineraViewSet
import docker_django.router as baseRouter


baseRouter.router.register(r'gasolinera', MarcaAutoViewSet, 'gasolinera')



urlpatterns = [
#    url(r'^marca-auto/(?P<pk>[0-9])/modelo-auto$', ModelosByMarcaView.as_view()),
]
