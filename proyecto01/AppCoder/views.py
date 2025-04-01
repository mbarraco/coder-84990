
from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes-list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'AppCoder/estudiante-detail.html', {'estudiante': estudiante})