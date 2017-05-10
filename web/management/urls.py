from django.conf.urls import url


from auto.views import MarcaAutoViewSet, ModeloAutoViewSet
from management.views import PersonaViewSet

import docker_django.router as baseRouter

baseRouter.router.register(r'persona', PersonaViewSet, 'persona')


urlpatterns = [
]

urlpatterns += baseRouter.router.urls


