import json
import requests
import os
from tabulate import tabulate
import re
import modules.getPagos as gPa

def postPago():
    # json-server storage/pago.json -b 5505
    pago = dict()
    while True:
     try:
        if(not pago.get("codigo_cliente")):
           codigo = input("Ingrese el codigo del cliente: " )
           if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
              data = gPa.getPagoCodigo(codigo)
              if(data):
                  print(tabulate(data, headers="keys", tablefmt="github"))
                  raise Exception("El codigo del cliente ya existe")
              else:
                   pago["codigo_cliente"] = codigo
           else:
                raise Exception("El codigo del cliente no cumple con el estandar establecido")
           
        if(not pago.get("forma_pago")):
            formaPago = input("Ingrese la forma de pago: ")
            if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                pago["forma_pago"] = formaPago
                break
            else:
                raise Exception("La forma de pago no cumple con el estandar establecido")
            
     except Exception as error:
        print(error)

    print(pago)

def menu():
 while True:
    print("""
    ___       __          _       _      __                 __                  __      __                    __                                    
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /___ _/ /_____  _____   ____/ /__     ____  ____ _____ _____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/\__,_/\__, /\____/____/  
                                                                                                                   /_/          /____/              
  

                                                            1. Administrar pagos
                                                            0. Regresar





""")   
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postPago(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break