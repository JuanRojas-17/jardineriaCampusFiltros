import json
import requests
import re
from tabulate import tabulate

def getAllGama():
    # json-server storage/producto.json -b 5502
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    data = getAllGama
    for val in data():
        gamaNombre.append(val.get("gama"))
    return gamaNombre

def menu():
 while True:
    print("""
        
    ____                        __              __        __                                   __               __          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                                       /_/                                     
  
        

                            1. Gamas disponibles
                            0. Regresar
""")
    
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                print(tabulate(getAllNombre(), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break