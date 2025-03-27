from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "todos/index.html")

def htmx(request):
  return render(request, "todos/htmx.html")