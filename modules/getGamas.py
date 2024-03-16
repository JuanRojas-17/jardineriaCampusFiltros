import json
import requests

def getAllGama():
    # json-server storage/producto.json -b 5502
    peticion = requests.get("http://192.168.10.13:5507")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    data = getAllGama
    for val in data():
        gamaNombre.append(val.get("gama"))
    return gamaNombre