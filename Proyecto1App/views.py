from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def index(request):
    estudiantes = Student.objects.all()
    context = {'clase': 'listado de estudiantes', 'estudiantes': estudiantes}
    return render(request, 'lista_estudiantes.html', context)