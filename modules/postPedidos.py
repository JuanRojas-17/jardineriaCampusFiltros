import json
import requests
import os
from tabulate import tabulate
import re
import modules.getPedidos as gPe

def postPedidos():
    # json-server storage/pedido.json -b 5506
    pedido = dict()
    while True:
     try:
        if(not pedido.get("codigo_pedido")):
           codigo = input("Ingrese el codigo del pedido: " )
           if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
              data = gPe.getPedidoCodigo(codigo)
              if(data):
                  print(tabulate(data, headers="keys", tablefmt="github"))
                  raise Exception("El codigo del pedido ya existe")
              else:
                   pedido["codigo_pedido"] = codigo
           else:
                raise Exception("El codigo del pedido no cumple con el estandar establecido")
           
        if(not pedido.get("nombre")):
            nombre = input("Ingrese el nombre del pedido: ")
            if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                pedido["nombre"] = nombre
                break
            else:
                raise Exception("El nombre del pedido no cumple con el estandar establecido")
            
     except Exception as error:
        print(error)

    print(pedido)

def menu():
 while True:
    print("""
    ___       __          _       _      __                 __                  __      __                    __                       ___     __          
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /___ _/ /_____  _____   ____/ /__     ____  ___  ____/ (_)___/ /___  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ _ \/ __  / / __  / __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/\___/\__,_/_/\__,_/\____/____/  
                                                                                                                   /_/                                     

                                                            1. Administrar pedidos
                                                            0. Regresar





""")   
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postPedidos(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break