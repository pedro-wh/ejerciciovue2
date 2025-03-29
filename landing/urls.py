from django.conf.urls import url

from landing.views import index

urlpatterns = [
    url(r'^$', index, name="index")
]