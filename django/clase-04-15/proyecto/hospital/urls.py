from django.urls import path

from hospital.views import (
    oftalmologia, 
    pediatria, 
    cirugia, 
    psi, 
    kinesiologia, 
    alta_medico, 
    lista_medico,
    buscar_medico,
    # 2025-04-15
    home,
    HospitalMedicoCreateView,
    HospitalMedicoListView,
    HospitalMedicoDetailView,
    HospitalMedicoUpdateView,
    HospitalMedicoDeleteView,
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
    # clase 2014-04-15
    path("home", home, name="home"),
    path("cbv/alta-medico", HospitalMedicoCreateView.as_view(), name="cbv-alta-medico"),
    path("cbv/lista-medico", HospitalMedicoListView.as_view(), name="cbv-lista-medico"),
    path("cbv/medico/<int:pk>", HospitalMedicoDetailView.as_view(), name="cbv-medico-detail"),
    path("cbv/medico/<int:pk>/editar", HospitalMedicoUpdateView.as_view(), name="cbv-medico-editar"),
    path("cbv/medico/<int:pk>/eliminar", HospitalMedicoDeleteView.as_view(), name="cbv-medico-eliminar"),
]
