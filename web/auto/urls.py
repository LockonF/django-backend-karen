from django.conf.urls import url

from auto.views import MarcaAutoViewSet, ModeloAutoViewSet, AutoViewSet, ModelosByMarcaView, MyAutosView
import docker_django.router as baseRouter


baseRouter.router.register(r'marca-auto', MarcaAutoViewSet, 'marca-auto')
baseRouter.router.register(r'modelo-auto', ModeloAutoViewSet, 'modelo-auto')
baseRouter.router.register(r'auto', AutoViewSet, 'auto')


urlpatterns = [
   url(r'^marca-auto/(?P<pk>[0-9])/modelo-auto$', ModelosByMarcaView.as_view()),
   url(r'^my-autos', MyAutosView.as_view()),
]
