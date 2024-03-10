import storage.cliente as cli
from tabulate import tabulate

def search():
    clienteName = []
    for val in cli.cliente:
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
    return clienteName

def getOneClienteCodigo(codigo):
    for val in cli.cliente:
        if(val.get('codigo_cliente')==codigo):
            return {
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        }

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.cliente:
        if(val.get('limit_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic

def getAllClientePaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    for val in cli.cliente:
        if(
           val.get('pais') == pais and 
           (val.get('region') == region or val.get('region') == None) or
           (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone

# Devuelve un listado con el nombre de los todos 
# los clientes españoles

def getAllNombrePais():
    nombrePais = []
    for val in cli.cliente:
        if(val.get("pais") == "Spain" ):
            nombrePais.append({
                "nombre_cliente": val.get("nombre_cliente"),
                "pais": val.get("pais")
            })
    return nombrePais

def menu():
    print("""
        

    ____                        __              __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                                
        

                                   1. Clientes españoles

""")
    
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllNombrePais(), headers="keys", tablefmt="github"))
    else:
        print("Opcion incorrecta")