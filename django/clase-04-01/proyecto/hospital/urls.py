from django.urls import path

from hospital.views import oftalmologia, pediatria

urlpatterns = [
    path("oftalmologia", oftalmologia, name="oftalmologia"),
    path("pediatria", pediatria, name="pediatria")
]
