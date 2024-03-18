import json
import requests
import os
from tabulate import tabulate
import re

def postGamas():
    gama = {}
    while True:
        try:
            nombre_gama = input("1. Ingrese el nombre de la gama: ")
            if not nombre_gama:
                raise ValueError("El nombre de la gama no puede estar vacío.")
            gama["gama"] = nombre_gama

            descripcion_texto = input("2. Ingrese una descripción textual de la gama: ")
            if not descripcion_texto:
                raise ValueError("La descripción textual no puede estar vacía.")
            gama["descripcion_texto"] = descripcion_texto

            descripcion_html = input("3. Ingrese una descripción HTML de la gama (opcional): ")
            gama["descripcion_html"] = descripcion_html if descripcion_html else None

            imagen = input("4. Ingrese el enlace de una imagen para la gama (opcional): ")
            gama["imagen"] = imagen if imagen else None

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, siga las instrucciones y asegúrese de ingresar los datos correctamente.")

    print("\nDatos de la gama ingresados con éxito. Aquí están los detalles:")
    print(gama)

if __name__ == "__main__":
    postGamas()

def menu():
 while True:
    os.system("clear")
    print("""
    ___       __          _       _      __                 __                  __            __      __                    __                                        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     ____/ /___ _/ /_____  _____   ____/ /__     ____ _____ _____ ___  ____ ______
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ `/ __ `/ __ `__ \/ __ `/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /_/ / / / / / / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \__,_/\__,_/\__/\____/____/   \__,_/\___/   \__, /\__,_/_/ /_/ /_/\__,_/____/  
                                                                                                                                  /____/                              
  


                                                    1. Administrar gamas
                                                    0. Atras


            """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postGamas(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break