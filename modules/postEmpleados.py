import json
import requests
import os
from tabulate import tabulate
import re
import modules.getEmpleados as ge

def conexionEmpleadojson():
      peticion=requests.get("http://192.168.10.23:5003") 
      Informacion=peticion.json()  
      return Informacion  

def postEmpleados():
    empleado = {}
    while True:
        try:
            codigo_empleado = int(input("1. Ingrese el código del empleado (número entero): "))
            empleado["codigo_empleado"] = codigo_empleado

            nombre = input("2. Ingrese el nombre del empleado: ")
            if not nombre:
                raise ValueError("El nombre del empleado no puede estar vacío.")
            empleado["nombre"] = nombre

            apellido1 = input("3. Ingrese el primer apellido del empleado: ")
            if not apellido1:
                raise ValueError("El primer apellido del empleado no puede estar vacío.")
            empleado["apellido1"] = apellido1

            apellido2 = input("4. Ingrese el segundo apellido del empleado: ")
            if not apellido2:
                raise ValueError("El segundo apellido del empleado no puede estar vacío.")
            empleado["apellido2"] = apellido2

            extension = input("5. Ingrese la extensión del empleado: ")
            if not extension:
                raise ValueError("La extensión del empleado no puede estar vacía.")
            empleado["extension"] = extension

            email = input("6. Ingrese el correo electrónico del empleado: ")
            if not email:
                raise ValueError("El correo electrónico del empleado no puede estar vacío.")
            empleado["email"] = email

            codigo_oficina = input("7. Ingrese el código de la oficina del empleado: ")
            if not codigo_oficina:
                raise ValueError("El código de la oficina del empleado no puede estar vacío.")
            empleado["codigo_oficina"] = codigo_oficina

            codigo_jefe = input("8. Ingrese el código del jefe del empleado (opcional): ")
            empleado["codigo_jefe"] = codigo_jefe if codigo_jefe else None

            puesto = input("9. Ingrese el puesto del empleado: ")
            if not puesto:
                raise ValueError("El puesto del empleado no puede estar vacío.")
            empleado["puesto"] = puesto

            break
        
        except ValueError as error:
            print("Error:", error)
            print("Por favor, siga las instrucciones y asegúrese de ingresar los datos correctamente.")

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://192.168.10.23:5003",headers=headers, data=json.dumps(empleado, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

if __name__ == "__main__":
    postEmpleados()

def deleteEmpleado(id):
    data = ge.getEmpleadoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://192.168.10.23:5003/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Empleado eliminado correctamete"})
            return{
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"Empleado no encontrado",
                "id": id
            }],
            "status": 400,
        }

def menu():
 while True:
    os.system("clear")
    print("""
    ___       __          _       _      __                 __                  __            __      __                    __                             __               __          
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     ____/ /___ _/ /_____  _____   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \__,_/\__,_/\__/\____/____/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                                                                                                                /_/                                     
 


                                                    1. Agregar empleados
                                                    2. Eliminar empleados
                                                    0. Atras


            """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postEmpleados(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 2):
               idEmpleado = int(input("Ingrese la id del empleado: "))
               print(tabulate(deleteEmpleado(idEmpleado), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break