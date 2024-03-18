import json
import requests
import os
from tabulate import tabulate
import re

def postProducto():
    # json-server storage/pedido.json -b 5501
    producto = {}
    while True:
        try:
            codigo = input("Ingrese el código del producto (formato: AA-111): ")
            if not re.match(r'^[A-Z]{2}-\d{3}$', codigo):
                raise ValueError("El código del producto debe tener el formato AA-111.")
            producto["codigo_producto"] = codigo

            nombre = input("Ingrese el nombre del producto: ")
            if not nombre:
                raise ValueError("El nombre del producto no puede estar vacío.")
            producto["nombre"] = nombre

            print("Seleccione la gama del producto:")
            print("1. Ornamentales")
            print("2. Herramientas")
            print("3. Aromáticas")
            opcion_gama = input("Ingrese el número correspondiente a la gama: ")
            if opcion_gama == "1":
                gama = "Ornamentales"
            elif opcion_gama == "2":
                gama = "Herramientas"
            elif opcion_gama == "3":
                gama = "Aromáticas"
            else:
                raise ValueError("Opción de gama inválida.")
            producto["gama"] = gama

            dimensiones = input("Ingrese las dimensiones del producto: ")
            producto["dimensiones"] = dimensiones

            proveedor = input("Ingrese el proveedor del producto: ")
            if not proveedor:
                raise ValueError("El proveedor del producto no puede estar vacío.")
            producto["proveedor"] = proveedor

            descripcion = input("Ingrese la descripción del producto: ")
            producto["descripcion"] = descripcion

            cantidad_en_stock = int(input("Ingrese la cantidad en stock del producto: "))
            if cantidad_en_stock <= 0:
                raise ValueError("La cantidad en stock debe ser un número entero mayor que cero.")
            producto["cantidad_en_stock"] = cantidad_en_stock

            precio_venta = float(input("Ingrese el precio de venta del producto: "))
            if precio_venta <= 0:
                raise ValueError("El precio de venta debe ser un número positivo.")
            producto["precio_venta"] = precio_venta

            precio_proveedor = float(input("Ingrese el precio del proveedor del producto: "))
            if precio_proveedor <= 0:
                raise ValueError("El precio del proveedor debe ser un número positivo.")
            producto["precio_proveedor"] = precio_proveedor

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, ingrese los datos correctamente.")

    print("Producto ingresado con éxito:", producto)

if __name__ == "__main__":
    postProducto()

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


                                                    1. Administrar productos
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

