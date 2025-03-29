from django.conf.urls import url

from htmx.views import htmx_delete, index


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^htmx_delete/(?P<id>\d+)/$', htmx_delete, name="index"),
]