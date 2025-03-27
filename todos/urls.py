from todos.views import htmx, htmx_replace, index
from django.conf.urls import url


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^htmx/$', htmx, name="htmx"),
    url(r'^htmx_replace/$', htmx_replace, name="htmx_replace"),
]