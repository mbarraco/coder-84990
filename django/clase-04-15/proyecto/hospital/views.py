from django.shortcuts import render

# Create your views here.

def oftalmologia(request): # en django se llama "view"
    return render(request, 'hospital/oftalmologia.html')


def pediatria(request):

    la_lista_de_pediatras = {
        "integrantes": [
            "Dr. Basso Alejandro",
            "Dr. Sololinsky Ricardo",
            "Dra. Avila Roxana",
            "Dr. Frank N. Furter."
        ]
    }


    return render(request, 'hospital/pediatria.html', context=la_lista_de_pediatras)


def cirugia(request):
    contexto = {
        "integrantes": [
            "Dr. Basso Alejandro", # cada integrante es un string
            "Dr. Sololinsky Ricardo",
            "Dra. Avila Roxana",
            "Dr. Frank N. Furter.",
            "Dr. Stein",
            "Dr. Strange"
        ]
    }
    return render(request, 'hospital/cirugia.html', context=contexto)


def psi(request):
    contexto = {
        "integrantes": [
            {"email": "a@hospital.com", "nombre": "Dr. Basso Alejandro"}, # cada integrante es un dict
            {"email": "b@hospital.com", "nombre": "Dr. Sololinsky Ricardo"},
            {"email": "c@hospital.com", "nombre": "Dra. Avila Roxana"},
            {"email": "d@hospital.com", "nombre": "Dr. Frank N. Furter."},
            {"email": "e@hospital.com", "nombre": "Dr. Stein"},
            {"email": "f@hospital.com", "nombre": "Dr. Strange"},
        ]
    }
    return render(request, 'hospital/psi.html', context=contexto)


def kinesiologia(request):
    return render(request, 'hospital/kinesiologia.html')


from hospital.forms import HospitalMedicoForm, HospitalMedicoBusquedaForm
from hospital.models import HospitalMedico
from django.shortcuts import redirect

def alta_medico(request):

    if request.method == "GET":
        print("." * 100)
        print("El metodo fue un get!")
        print("." * 100)

        contexto = {"formulario": HospitalMedicoForm()}
        return render(request, 'hospital/form_medico.html', context=contexto)
    else:
        print(">" * 100)
        print("El metodo fue POST")
        print(request.POST)
        print(">" * 100)

        formulario = HospitalMedicoForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_de_base_de_datos = HospitalMedico(
                nombre=datos["nombre"],
                email=datos["email"],
                antiguedad=datos["antiguedad"]
            )
            modelo_de_base_de_datos.save()

            return redirect("hospital:lista-medico")


def lista_medico(request):

    modelos = HospitalMedico.objects.all()
    contexto = {
        "integrantes": modelos
    }
    return render(request, 'hospital/lista_medico.html', context=contexto)


def buscar_medico(request):
    if request.method == "GET":
       contexto = {"formulario": HospitalMedicoBusquedaForm()}
       return render(request, 'hospital/buscar_medico.html', context=contexto)
    else:
        # procesamos el formulario y devolvemos un resultado
        formulario = HospitalMedicoBusquedaForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            medicos = HospitalMedico.objects.filter(nombre__icontains=nombre)

            contexto = {
                "medicos": medicos,
            }
            return render(request, 'hospital/detail_medico.html', context=contexto)
        
        # si no es válido, volvemos a mostrar el form con errores
        contexto = {"formulario": HospitalMedicoBusquedaForm()}
        return render(request, 'hospital/buscar_medico.html', context=contexto)