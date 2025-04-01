
from django.urls import path
from .views import lista_productos, detalle_producto, index


urlpatterns = [
    path("index", index, name="index"),
    path('productos/', lista_productos, name='producto-lista'),
    path('productos/<int:pk>/', detalle_producto, name='producto-detalle'),
]