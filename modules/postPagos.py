import json
import requests
import os
from tabulate import tabulate
import re
import modules.getPagos as gPa

def postPago():
    # json-server storage/pedido.json -b 5505
    pago = {}
    while True:
        try:
            codigo_cliente = int(input("Ingrese el código del cliente (número entero positivo): "))
            if codigo_cliente <= 0:
                raise ValueError("El código del cliente debe ser un número entero positivo.")
            pago["codigo_cliente"] = codigo_cliente

            forma_pago = input("Ingrese la forma de pago: ")
            pago["forma_pago"] = forma_pago

            id_transaccion = input("Ingrese el ID de transacción: ")
            pago["id_transaccion"] = id_transaccion

            fecha_pago = input("Ingrese la fecha de pago (formato: YYYY-MM-DD): ")
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_pago):
                raise ValueError("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            pago["fecha_pago"] = fecha_pago

            total = float(input("Ingrese el monto total del pago (número positivo): "))
            if total <= 0:
                raise ValueError("El monto total debe ser un número positivo.")
            pago["total"] = total

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, ingrese los datos correctamente.")

    print("Pago ingresado con éxito:", pago)

if __name__ == "__main__":
    postPago()

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