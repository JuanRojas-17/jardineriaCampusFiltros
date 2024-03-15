import storage.empleado as em
from tabulate import tabulate
import re

# Devuelve un lista con el nombre, apellidos y email
# de los empleados cuyo jefe tiene un codigo de jefe igual a 7.

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleado:
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

# 4

def getAllPuestoNombreApellidoEmailJefe():
    puestoNombreApellidoEmailJefe = []
    for val in em.empleado:
        if val.get("codigo_jefe") == None:
            puestoNombreApellidoEmailJefe.append({
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": val.get("apellido1"),
                "email": val.get("email"),
            })
    return puestoNombreApellidoEmailJefe

#5

def getAllNombreApellidoPuestoEmpleadosNoRepresentatesDeVentas():
    nombreApellidoPuesto = []
    for val in em.empleado:
        if val.get("puesto") != "Representante Ventas":
            nombreApellidoPuesto.append({
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "puesto": val.get("puesto")
            })
    return nombreApellidoPuesto

def menu():
 while True:
    print("""
        
    ____                        __              __        __                                   __               __          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                                       /_/                                     
  
        

                            1. Informacion empleados con codigo de jefe
                            2. Informacion jefe
                            3. Informacion empleados no representantes de ventas
                            0. Regresar
""")
    
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                codigo = int(input("Introduzca el codigo de jefe: "))
                print(tabulate(getAllNombreApellidoEmailJefe(codigo), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getAllPuestoNombreApellidoEmailJefe(), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                print(tabulate(getAllNombreApellidoPuestoEmpleadosNoRepresentatesDeVentas(), headers="keys", tablefmt="github" ))
            elif(opcion == 0):
                break