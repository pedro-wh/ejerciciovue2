from django.shortcuts import render

from api.models import Column

# Create your views here.
def index(request):
  columns = Column.objects.prefetch_related("todos").all()
  context = {"columns": columns}
  return render(request, "jquery/index.html", context)