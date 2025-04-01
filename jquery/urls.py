from django.conf.urls import url

from jquery.views import jquery_createTodo, jquery_delete, index, jquery_moveTodo


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^jquery_delete/(?P<id>\d+)/$', jquery_delete, name="index"),
    url(r'^jquery_createTodo/(?P<id>\d+)/$', jquery_createTodo, name="create"),
    url(r'^jquery_moveTodo/(?P<idTodo>\d+)/(?P<idColumn>\d+)/$', jquery_moveTodo, name="edit"),
]