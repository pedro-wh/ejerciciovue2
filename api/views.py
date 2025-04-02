from rest_framework import viewsets

from api.models import Column, Todo
from api.serializer import ColumnSerializer, TodoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class ColumnAPI(viewsets.ModelViewSet):
  queryset = Column.objects.prefetch_related("todos").all()
  serializer_class = ColumnSerializer


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class TodoAPI(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer