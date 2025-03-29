from django.conf.urls import url

from htmx.views import index


urlpatterns = [
    url(r'^$', index, name="index"),
]