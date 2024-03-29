from tabulate import tabulate
import json
import requests
import os
import re

def getAllData():
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data

def getProductoCodigo(id):
        peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
        return(peticion.json()) if peticion.ok else []

# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
# y que tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio.


# def getProductoCodigo(id):
#       data = getAllData()
#       for val in data:
#           if(val.get('codigo_producto') == id):
#               return [val]

def getAllStocksPriceGama(gama, stock):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock_gte={stock}&_sort=-precio_venta")
    condiciones = peticion.json()

    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones

def menu():
 while True:
    print("""
          
    ____                        __              __        __                                   __           __            
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   ____  _________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                        /_/                                                  

              1. Informacion productos de una misma categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea superior
              0. Atras
              
              """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                gama = input("Ingrese la gama que deseas filtrar: ")
                stock = int(input("Ingrese las unidades que desea mostrar: "))
                print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break