import storage.oficina as of
from tabulate import tabulate

# Devuelve un listado con el codigo de
# oficina y la ciudad donde hay oficinas.

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo_oficina": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Devuelve un listado con la ciudad y el telefono
# de las oficinas de España
        
def getAllCiudadTelefono(pais):
        ciudadTelefono = []
        for val in of.oficina:
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
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="github"))
    elif(opcion == 2):
        pais = "España"
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))
    elif(opcion == 0):
        break
    