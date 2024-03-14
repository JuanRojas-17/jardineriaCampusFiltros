import json

def postProducto(producto):
    import requests
    peticion = requests.post("http://172.16.102.108:5501", data=json.dumps(producto))
    res = peticion.json()
    return res