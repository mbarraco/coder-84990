# Jugador numero 1: Server
from flask import Flask # pip install flask


server = Flask("Hospital")


@server.route("/oftalmologia")
def oftalmologia():
    return "Hola, tiene bien sus ojos?"

@server.route("/pediatria")
def pediatria():
    return "Hola, cuantos años tiene el niño o niña?"

server.run(debug=True)
