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
    return HttpResponse("")
  return HttpResponse(status=405)

def htmx_createTodo(request, id):
  if request.method == "POST":
    todo = Todo(column_id=id, name="Tarea Nueva")
    todo.save()
    context = {"item": todo}
    return render(request, "htmx/createTodo.html", context)
  
def htmx_editTodo(request, id):
  todo = Todo.objects.get(id=id)
  context = {"item": todo}
  if request.method == "POST":
    todo.name = request.POST["nombredeltodo"]
    todo.save()
    return render(request, "htmx/editTodoResponse.html", context)
  return render(request, "htmx/editTodo.html", context)