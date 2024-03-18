import json
import requests
import os
from tabulate import tabulate
import re
# 5502

def postClientes():
    cliente = {}
    while True:
        try:
            codigo_cliente = int(input("1. Ingrese el código del cliente (número entero): "))
            cliente["codigo_cliente"] = codigo_cliente

            nombre_cliente = input("2. Ingrese el nombre del cliente: ")
            if not nombre_cliente:
                raise ValueError("El nombre del cliente no puede estar vacío.")
            cliente["nombre_cliente"] = nombre_cliente

            nombre_contacto = input("3. Ingrese el nombre del contacto: ")
            if not nombre_contacto:
                raise ValueError("El nombre del contacto no puede estar vacío.")
            cliente["nombre_contacto"] = nombre_contacto

            apellido_contacto = input("4. Ingrese el apellido del contacto: ")
            if not apellido_contacto:
                raise ValueError("El apellido del contacto no puede estar vacío.")
            cliente["apellido_contacto"] = apellido_contacto

            telefono = input("5. Ingrese el número de teléfono del cliente: ")
            if not telefono:
                raise ValueError("El número de teléfono del cliente no puede estar vacío.")
            cliente["telefono"] = telefono

            fax = input("6. Ingrese el número de fax del cliente (opcional): ")
            cliente["fax"] = fax if fax else None

            linea_direccion1 = input("7. Ingrese la primera línea de la dirección del cliente: ")
            if not linea_direccion1:
                raise ValueError("La primera línea de la dirección del cliente no puede estar vacía.")
            cliente["linea_direccion1"] = linea_direccion1

            linea_direccion2 = input("8. Ingrese la segunda línea de la dirección del cliente (opcional): ")
            cliente["linea_direccion2"] = linea_direccion2 if linea_direccion2 else None

            ciudad = input("9. Ingrese la ciudad del cliente: ")
            if not ciudad:
                raise ValueError("La ciudad del cliente no puede estar vacía.")
            cliente["ciudad"] = ciudad

            region = input("10. Ingrese la región del cliente (opcional): ")
            cliente["region"] = region if region else None

            pais = input("11. Ingrese el país del cliente: ")
            if not pais:
                raise ValueError("El país del cliente no puede estar vacío.")
            cliente["pais"] = pais

            codigo_postal = input("12. Ingrese el código postal del cliente: ")
            if not codigo_postal or len(codigo_postal) != 5:
                raise ValueError("El código postal del cliente debe tener 5 dígitos.")
            cliente["codigo_postal"] = codigo_postal

            codigo_empleado_rep_ventas = int(input("13. Ingrese el código del empleado representante de ventas (número entero): "))
            cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas

            limite_credito = float(input("14. Ingrese el límite de crédito del cliente: "))
            if limite_credito <= 0:
                raise ValueError("El límite de crédito del cliente debe ser un número positivo.")
            cliente["limite_credito"] = limite_credito

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, siga las instrucciones y asegúrese de ingresar los datos correctamente.")

    print("\nDatos del cliente ingresados con éxito. Aquí están los detalles:")
    print(cliente)

if __name__ == "__main__":
    postClientes()

def menu():
 while True:
    os.system("clear")
    print("""
    ___       __          _       _      __                 __                  __            __      __                    __             ___            __           
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     ____/ /___ _/ /_____  _____   ____/ /__     _____/ (_)__  ____  / /____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \__,_/\__,_/\__/\____/____/   \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/  
                                                                                                                                                                       



                                                    1. Administrar clientes
                                                    0. Atras


            """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postClientes(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break