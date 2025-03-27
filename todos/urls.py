from todos.views import htmx, index
from django.conf.urls import url


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^htmx/$', htmx, name="htmx"),
]