from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from api.models import Column, Todo

# Create your views here.
def index(request):
  columns = Column.objects.prefetch_related("todos").all()
  context = {"columns": columns}
  return render(request, "jquery/index.html", context)


def jquery_delete(request, id):
  if request.method == "DELETE":
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return HttpResponse(status=200)
  return HttpResponse(status=200)

def jquery_createTodo(request, id):
  if request.method == "POST":
    todo = Todo(column_id=id, name="Tarea Nueva")
    todo.save()
    return JsonResponse({"id": todo.id, "name": todo.name, "column_id": todo.column_id})


def jquery_moveTodo(request, idTodo, idColumn):
  todo = Todo.objects.get(id=idTodo)
  todo.column_id = idColumn
  todo.save()
  return HttpResponse(status=200)