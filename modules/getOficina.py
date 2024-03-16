import requests
from tabulate import tabulate
import re
import json

def dataOficina():
    peticion = requests.get("http://192.168.10.13:5504")
    data = peticion.json()
    return data

# Devuelve un listado con el codigo de
# oficina y la ciudad donde hay oficinas.

def getAllCodigoCiudad():
    codigoCiudad = []
    data = dataOficina()
    for val in data:
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Devuelve un listado con la ciudad y el telefono
# de las oficinas de España
        
def getAllCiudadTelefono(pais):
        ciudadTelefono = []
        data = dataOficina()
        for val in data:
            if(val.get("pais") == pais ):
                ciudadTelefono.append({
                    "ciudad": val.get("ciudad"),
                    "telefono": val.get("telefono"),
                    "oficina": val.get("codigo_oficina"),
                    "pais": val.get("pais")
                })
        return ciudadTelefono
    
def menu():
 while True:
    print("""
        
    ____                        __              __        __                    _____      _                 
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___ ______   ____  / __(_)____(_)___  ____ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ `/ ___/  / __ \/ /_/ / ___/ / __ \/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\__,_/____/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
          /_/                                                                                                

        

                                   1. Informacion oficinas
                                   2. Informacion oficinas de España
                                   0. Regresar

""")
    
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                pais = "España"
                print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break
    