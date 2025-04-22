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
    # 2025-04-22
    about
)


app_name = "hospital"

urlpatterns = [
    path("hospital/oftalmologia", oftalmologia, name="oftalmologia"),
    path("hospital/pediatria", pediatria, name="pediatria"),
    path("hospital/cirugia", cirugia, name="cirugia"),
    path("hospital/psi", psi, name="psi"),
    path("hospital/kinesiologia", kinesiologia, name="kinesiologia"),
    path("hospital/alta-medico", alta_medico, name="alta-medico"),
    path("hospital/lista-medico", lista_medico, name="lista-medico"),
    path("hospital/buscar-medico", buscar_medico, name="buscar-medico"),
    # clase 2014-04-15
    path('', home, name='root'),
    path('hospital/', home, name='root'),
    path("hospital/cbv/alta-medico", HospitalMedicoCreateView.as_view(), name="cbv-alta-medico"),
    path("hospital/cbv/lista-medico", HospitalMedicoListView.as_view(), name="cbv-lista-medico"),
    path("hospital/cbv/medico/<int:pk>", HospitalMedicoDetailView.as_view(), name="cbv-medico-detail"),
    path("hospital/cbv/medico/<int:pk>/editar", HospitalMedicoUpdateView.as_view(), name="cbv-medico-editar"),
    path("hospital/cbv/medico/<int:pk>/eliminar", HospitalMedicoDeleteView.as_view(), name="cbv-medico-eliminar"),
    # Clase 22 de Abril 
    path("about", about, name="about")
]
