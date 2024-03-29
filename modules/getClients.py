import requests
from tabulate import tabulate
import re
import json

def dataClientes():
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

def search():   
    clienteName = []
    data = dataClientes()
    for val in data:
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
    return clienteName

def getClienteCodigo(id):
        peticion = requests.get(f"http://154.38.171.54:5001/cliente/{id}")
        return(peticion.json()) if peticion.ok else []

def getOneClienteCodigo(codigo):
    clientecode= []
    data = dataClientes()
    for val in data:
        dataclient = {
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "nombre_contacto": val.get('nombre_contacto'),
            "apellido_contacto": val.get("apellido_contacto"),
            "telefono": val.get('telefono'),
            "fax": val.get('fax')}
        if(val.get('codigo_cliente') == codigo):
            clientecode.append(dataclient)
    return clientecode
         

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = []
    data = dataClientes()
    for val in data:
        dataclient = {
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "nombre_contacto": val.get('nombre_contacto'),
            "apellido_contacto": val.get("apellido_contacto"),
            "telefono": val.get('telefono'),
            "fax": val.get('fax'),
            "limite_credito": val.get('limite_credito'),
            "ciudad": val.get('ciudad')
            }
        if(val.get('limit_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(dataclient)
    return clienteCredic

def getAllClientePaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = list()
    data = dataClientes()
    for val in data:
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
    data = dataClientes()
    for val in data:
        if(val.get("pais") == "Spain" ):
            nombrePais.append({
                "nombre_cliente": val.get("nombre_cliente"),
                "pais": val.get("pais")
            })
    return nombrePais

def getAllInformacionCodigoEmpleado(codigo):
    empleadoCodigo = []
    data = dataClientes()
    for val in data:
        dataclient = {
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
            "nombre_contacto": val.get('nombre_contacto'),
            "apellido_contacto": val.get("apellido_contacto"),
            "telefono": val.get('telefono'),
            "fax": val.get('fax')}
        if(val.get('codigo_cliente') == codigo):
            empleadoCodigo.append(dataclient)
    return empleadoCodigo


def menu():
 while True:
    print("""
        

    ____                        __              __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                                
        

                                   1. Clientes españoles
                                   2. Informacion clientes segun codigo
                                   3. Informacion clientes segun codigo de empleado
                                   0. Regresar

""")
    
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                print(tabulate(getAllNombrePais(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                codigo = int(input("Ingrese el codigo del cliente: "))
                print(tabulate(getOneClienteCodigo(codigo), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                codigo = int(input("Ingrese el codigo del empleado: "))
                print(tabulate(getAllInformacionCodigoEmpleado(codigo), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break