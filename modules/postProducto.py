import json
import requests
import os
from tabulate import tabulate
import modules.getGamas as gG


def postProducto():
    # json-server storage/producto.json -b 5501
    producto = {
         "codigo_producto": input("Ingrese el codigo del producto: "),
         "nombre": input("Ingrese el nomnbre del producto: "),
         "gama": gG.getAllNombre()[int(input("Seleccione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
         "dimensiones": input("Ingrese las dimensiones del producto: "),
         "proveedor": input("Ingrese el proveedor del producto: "),
         "descripcion": input("Ingrese la descripcion del producto: "),
         "cantidad_en_stock": int(input("Ingrese la cantidad en stock del producto: ")),
         "precio_venta": int(input("Ingrese el precio de venta del producto: ")),
         "precio_proveedor": int(input("Ingrese el precio del proveedor del prodcuto: "))
    }

    peticion = requests.post("http://172.16.102.108:5501", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

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
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
     print(tabulate(postProducto(), headers="keys", tablefmt="github"))
     input("Presione una tecla para continuar: ")
    elif(opcion == 0):
     break

