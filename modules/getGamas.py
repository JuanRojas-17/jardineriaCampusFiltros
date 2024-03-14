import json
import requests

def getAllGama():
    # json-server storage/producto.json -b 5502
    peticion = requests.get("http://172.16.102.108:5502")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre