from django.shortcuts import render

# Create your views here.

def oftalmologia(request): # en django se llama "view"
    return render(request, 'hospital/oftalmologia.html')


def pediatria(request):
    xx = [
        {"nombre": "Miguel", "apellido": "Basso", "telefono": 6001234567},
        {"nombre": "Marcela", "apellido": "Lopez", "telefono": 6009876543},
        {"nombre": "Luis", "apellido": "Gomez", "telefono": 6001122334},
        {"nombre": "Ana", "apellido": "Martinez", "telefono": 6002233445},
        {"nombre": "Carlos", "apellido": "Garcia", "telefono": 6003344556},
        {"nombre": "Patricia", "apellido": "Rodriguez", "telefono": 6004455667},
        {"nombre": "Juan", "apellido": "Sanchez", "telefono": 6005566778},
        {"nombre": "Sofia", "apellido": "Perez", "telefono": 6006677889},
        {"nombre": "Javier", "apellido": "Fernandez", "telefono": 6007788990},
        {"nombre": "Elena", "apellido": "Basso", "telefono": 6008899001},
        {"nombre": "Miguel", "apellido": "Garcia", "telefono": 6009900112},
        {"nombre": "Marcela", "apellido": "Lopez", "telefono": 6001234432},
        {"nombre": "Luis", "apellido": "Rodriguez", "telefono": 6002345543},
        {"nombre": "Carlos", "apellido": "Sanchez", "telefono": 6003456654}
    ]

    contexto = {
        "pediatras": xx
    }
    return render(request, 'hospital/pediatria.html', context=contexto)
