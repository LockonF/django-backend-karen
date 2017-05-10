from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Autos API')


urlpatterns = [
    url(r'^api-doc$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('auto.urls', namespace='docker_django')),
    url(r'^',include('management.urls', namespace='docker_django'))
]
