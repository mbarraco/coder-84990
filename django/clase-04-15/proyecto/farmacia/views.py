from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def recetas_magistrales(_): # en django se llama "view"
    return HttpResponse("Hola, tiene una receta?")
