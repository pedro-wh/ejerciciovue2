from django.conf.urls import url

from jquery.views import index


urlpatterns = [
    url(r'^$', index, name="index"),
]