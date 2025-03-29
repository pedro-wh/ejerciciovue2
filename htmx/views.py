from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from api.models import Column, Todo

# Create your views here.
def index(request):
  columns = Column.objects.prefetch_related("todos").all()
  context = {"columns": columns}
  return render(request, "htmx/index.html", context)


def htmx_delete(request, id):
  if request.method == "DELETE":
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return HttpResponse(status=204)
  
  return HttpResponse(status=405)