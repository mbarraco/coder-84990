# Jugador numero 2: Client
import requests


url = "http://127.0.0.1:5000/oftalmologia"

response = requests.get(url)

print(response.status_code, "-- respuesta:",response.text)