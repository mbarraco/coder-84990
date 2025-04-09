from django.forms import ModelForm

from hospital.models import HospitalMedico


class HospitalMedicoForm(ModelForm):
    
    class Meta:
        model = HospitalMedico

        fields = ["nombre", "email", "antiguedad"]


class HospitalMedicoBusquedaForm(ModelForm):
    
    class Meta:
        model = HospitalMedico

        fields = ["nombre"]