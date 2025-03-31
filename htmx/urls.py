from django.conf.urls import url

from htmx.views import htmx_createTodo, htmx_delete, htmx_editTodo, htmx_moveTodo, index


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^htmx_delete/(?P<id>\d+)/$', htmx_delete, name="index"),
    url(r'^htmx_createTodo/(?P<id>\d+)/$', htmx_createTodo, name="create"),
    url(r'^htmx_editTodo/(?P<id>\d+)/$', htmx_editTodo, name="edit"),
    url(r'^htmx_moveTodo/(?P<idTodo>\d+)/(?P<idColumn>\d+)/$', htmx_moveTodo, name="edit"),
]