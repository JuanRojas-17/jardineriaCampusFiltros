import json
import requests
import os
from tabulate import tabulate
import re
import modules.getPedidos as gPe

def postPedidos():
    # json-server storage/pedido.json -b 5506
    pedido = {}
    while True:
        try:
            codigo_pedido = int(input("Ingrese el código del pedido: "))
            if codigo_pedido <= 0:
                raise ValueError("El código del pedido debe ser un número entero positivo.")
            pedido["codigo_pedido"] = codigo_pedido

            fecha_pedido = input("Ingrese la fecha del pedido (formato: YYYY-MM-DD): ")
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_pedido):
                raise ValueError("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            pedido["fecha_pedido"] = fecha_pedido

            fecha_esperada = input("Ingrese la fecha esperada de entrega (formato: YYYY-MM-DD): ")
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_esperada):
                raise ValueError("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            pedido["fecha_esperada"] = fecha_esperada

            fecha_entrega = input("Ingrese la fecha de entrega (dejar vacío si aún no se ha entregado) (formato: YYYY-MM-DD): ")
            if fecha_entrega and not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_entrega):
                raise ValueError("Formato de fecha incorrecto. Debe ser YYYY-MM-DD o dejar vacío.")
            pedido["fecha_entrega"] = fecha_entrega if fecha_entrega else None

            print("Seleccione el estado del pedido:")
            print("1. Pendiente")
            print("2. Entregado")
            print("3. Rechazado")
            opcion_estado = input("Ingrese el número correspondiente al estado: ")
            if opcion_estado == "1":
                estado = "Pendiente"
            elif opcion_estado == "2":
                estado = "Entregado"
            elif opcion_estado == "3":
                estado = "Rechazado"
            else:
                raise ValueError("Opción de estado inválida.")
            pedido["estado"] = estado

            comentario = input("Ingrese un comentario para el pedido: ")
            pedido["comentario"] = comentario

            codigo_cliente = int(input("Ingrese el código del cliente: "))
            if codigo_cliente <= 0:
                raise ValueError("El código del cliente debe ser un número entero positivo.")
            pedido["codigo_cliente"] = codigo_cliente

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, ingrese los datos correctamente.")

    print("Pedido ingresado con éxito:", pedido)

if __name__ == "__main__":
    postPedidos()

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