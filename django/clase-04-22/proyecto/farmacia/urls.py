from django.urls import path

from farmacia.views import recetas_magistrales


app_name = "farmacia"

urlpatterns = [
    path("recetas-magistrales", recetas_magistrales, name="recetas-magistrales")
]
