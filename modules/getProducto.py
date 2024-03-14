from tabulate import tabulate
import json
import requests
import modules.postProducto as psProducto
import modules.getGamas as gG

# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
# y que tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio.
def getAllData():
    peticion = requests.get("http://172.16.102.108:5501")
    data = peticion.json()
    return data

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse = True)
    for i, val in enumerate(condiciones):
            condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "nombre": f'{val["descripcion"][:5]}...',
                "gama": val.get("codigo_producto"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor"),
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

              1. Informacion productos de una misma gama con mas de 100 unidades en stock de manera descendente
              2. Guardar
              3. Regresar
              
              """)
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        gama = input("Ingrese la gama que deseas filtrar: ")
        stock = int(input("Ingrese las unidades que desea mostrar: "))
        print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="github"))
    elif(opcion == 2):
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
        psProducto.postProducto(producto)
        print("Producto Guardado")
    elif(opcion == 3):
        break