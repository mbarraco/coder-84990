from django.urls import path

from farmacia.views import recetas_magistrales

urlpatterns = [
    path("recetas-magistrales", recetas_magistrales)
]
