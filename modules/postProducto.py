import json
import requests
import os
from tabulate import tabulate
import modules.getGamas as gG
import re
import modules.getProducto as gP


def postProducto():
    # json-server storage/producto.json -b 5501
    producto = dict()
    while True:
     try:
        if(not producto.get("codigo_producto")):
           codigo = input("Ingrese el codigo del producto: " )
           if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
              data = gP.getProductoCodigo(codigo)
              if(data):
                  print(tabulate(data, headers="keys", tablefmt="github"))
                  raise Exception("EL codigo producto ya existe")
              else:
                   producto["codigo_producto"] = codigo
           else:
                raise Exception("El codigo producto no cumple con el estandar establecido")
           
        if(not producto.get("nombre")):
            nombre = input("Ingrese el nombre del producto: ")
            if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                producto["nombre"] = nombre
                break
            else:
                raise Exception("El nombre del producto no cumple con el estandar establecido")
            
     except Exception as error:
        print(error)

    print(producto)

   #     producto = {
   #         "codigo_producto": input("Ingrese el codigo del producto: "),
  #          "nombre": input("Ingrese el nomnbre del producto: "),
 #           "gama": gG.getAllNombre()[int(input("Seleccione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
  #          "dimensiones": input("Ingrese las dimensiones del producto: "),
  #          "proveedor": input("Ingrese el proveedor del producto: "),
  #          "descripcion": input("Ingrese la descripcion del producto: "),
  #          "cantidad_en_stock": int(input("Ingrese la cantidad en stock del producto: ")),
  #          "precio_venta": int(input("Ingrese el precio de venta del producto: ")),
  #          "precio_proveedor": int(input("Ingrese el precio del proveedor del prodcuto: "))
  #      }

   #     peticion = requests.post("http://172.16.102.108:5501", data=json.dumps(producto))
    #    res = peticion.json()
    #    res["Mensaje"] = "Producto Guardado"
    #    return [res]

def menu():
 while True:
    os.system("clear")
    print("""

    ___       __          _       _      __                 __                  __      __                    __                             __           __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /___ _/ /_____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                                                                                   /_/                                                  


                                                    1. Guardar un producto nuevo
                                                    0. Atras


            """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postProducto(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break

