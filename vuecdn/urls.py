from django.conf.urls import url
from vuecdn.views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]