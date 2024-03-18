import json
import requests
import os
from tabulate import tabulate
import re
# 5504

def postOficina():
    oficina = {}
    while True:
        try:
            codigo_oficina = input("1. Ingrese el código de la oficina (debe tener el formato ABC-XX): ")
            if not re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigo_oficina):
                raise ValueError("El código de la oficina debe tener el formato ABC-XX.")
            oficina["codigo_oficina"] = codigo_oficina

            ciudad = input("2. Ingrese la ciudad de la oficina: ")
            if not ciudad:
                raise ValueError("La ciudad no puede estar vacía.")
            oficina["ciudad"] = ciudad

            pais = input("3. Ingrese el país de la oficina: ")
            if not pais:
                raise ValueError("El país no puede estar vacío.")
            oficina["pais"] = pais

            region = input("4. Ingrese la región de la oficina: ")
            if not region:
                raise ValueError("La región no puede estar vacía.")
            oficina["region"] = region

            codigo_postal = input("5. Ingrese el código postal de la oficina (debe tener 5 dígitos): ")
            if not re.match(r'^\d{5}$', codigo_postal):
                raise ValueError("El código postal debe tener exactamente 5 dígitos.")
            oficina["codigo_postal"] = codigo_postal

            telefono = input("6. Ingrese el teléfono de la oficina (formato: +XX XXX XXXXXXX): ")
            if not re.match(r'^\+\d{2} \d{3} \d{7}$', telefono):
                raise ValueError("El teléfono debe tener el formato +XX XXX XXXXXXX.")
            oficina["telefono"] = telefono

            linea_direccion1 = input("7. Ingrese la línea de dirección 1 de la oficina: ")
            if not linea_direccion1:
                raise ValueError("La línea de dirección 1 no puede estar vacía.")
            oficina["linea_direccion1"] = linea_direccion1

            linea_direccion2 = input("8. Ingrese la línea de dirección 2 de la oficina (opcional): ")
            oficina["linea_direccion2"] = linea_direccion2

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, siga las instrucciones y asegúrese de ingresar los datos correctamente.")

    print("\nOficina ingresada con éxito. Aquí están los detalles de la oficina: ")
    print(oficina)

if __name__ == "__main__":
    postOficina()

def menu():
 while True:
    os.system("clear")
    print("""
    ___       __          _       _      __                 __                  __            __      __                    __              _____      _            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     ____/ /___ _/ /_____  _____   ____/ /__     ____  / __(_)____(_)___  ____ _
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ / 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \__,_/\__,_/\__/\____/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/  
                                                                                                                                                                    


                                                    1. Administrar oficinas
                                                    0. Atras


            """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postOficina(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break