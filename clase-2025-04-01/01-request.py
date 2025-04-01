import requests


url = "https://restcountries.com/v3.1/name/india"


response = requests.get(url)


print(response.status_code)

# ya averiguamos que es una lista
informacion = response.json()

# sabemos que el primer elemento de esa lista
# es un diccionario y tiene una clave "maps"

mapas = informacion[0]["maps"]

for empresa, mapa in mapas.items():
    print(empresa, mapa)