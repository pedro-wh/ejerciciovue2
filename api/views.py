from rest_framework import viewsets

from api.models import Column
from api.serializer import ColumnSerializer

# Create your views here.
class ColumnAPI(viewsets.ModelViewSet):
  queryset = Column.objects.all()
  serializer_class = ColumnSerializer