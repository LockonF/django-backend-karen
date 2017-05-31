from django.conf.urls import url


from auto.views import MarcaAutoViewSet, ModeloAutoViewSet
from management.views import PersonaViewSet, PersonaDataView

import docker_django.router as baseRouter

baseRouter.router.register(r'persona', PersonaViewSet, 'persona')


urlpatterns = [
    url(r'user-data', PersonaDataView.as_view()),

]

urlpatterns += baseRouter.router.urls


