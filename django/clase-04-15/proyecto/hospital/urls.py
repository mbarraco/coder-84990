from django.urls import path

from hospital.views import (
    oftalmologia, 
    pediatria, 
    cirugia, 
    psi, 
    kinesiologia, 
    alta_medico, 
    lista_medico,
    buscar_medico   
)


app_name = "hospital"

urlpatterns = [
    path("oftalmologia", oftalmologia, name="oftalmologia"),
    path("pediatria", pediatria, name="pediatria"),
    path("cirugia", cirugia, name="cirugia"),
    path("psi", psi, name="psi"),
    path("kinesiologia", kinesiologia, name="kinesiologia"),
    path("alta-medico", alta_medico, name="alta-medico"),
    path("lista-medico", lista_medico, name="lista-medico"),
    path("buscar-medico", buscar_medico, name="buscar-medico"),
]
