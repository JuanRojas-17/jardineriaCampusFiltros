import json
import requests
import os
from tabulate import tabulate
import re
import modules.getClients as gCl

def conexionClientejson():
      peticion=requests.get("http://154.38.171.54:5001/cliente") 
      Informacion=peticion.json()  
      return Informacion     

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

            codigo_postal = input("12. Ingrese el código postal del cliente(5 digitos): ")
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

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5001/cliente",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Cliente Guardado"
    return [res]

if __name__ == "__main__":
    postClientes()

def deleteCliente(id):
    data = gCl.getClienteCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Cliente eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code
            }
    else:
        return {
            "body": [{
                "message": "Cliente no encontrado",
                "id": id
            }],
            "status": 400
        }
    
def actualizarCliente(id):
    clienteExistente = gCl.getClienteCodigo(id)
    print(clienteExistente)
    if len(clienteExistente) == 0:
        return {"message": "Cliente no encontrado"}

    cliente = {}
    
    print("Ingrese los nuevos datos del cliente:")
    
    cliente["codigo_cliente"] = int(input("Ingrese el nuevo código del cliente: "))
    cliente["nombre_cliente"] = input("Ingrese el nuevo nombre del cliente: ")
    cliente["nombre_contacto"] = input("Ingrese el nuevo nombre de contacto: ")
    cliente["apellido_contacto"] = input("Ingrese el nuevo apellido de contacto: ")
    cliente["telefono"] = input("Ingrese el nuevo número de teléfono: ")
    cliente["fax"] = input("Ingrese el nuevo número de fax: ")
    cliente["linea_direccion1"] = input("Ingrese la nueva línea de dirección 1: ")
    cliente["linea_direccion2"] = input("Ingrese la nueva línea de dirección 2: ")
    cliente["ciudad"] = input("Ingrese la nueva ciudad: ")
    cliente["region"] = input("Ingrese la nueva región: ")
    cliente["pais"] = input("Ingrese el nuevo país: ")
    cliente["codigo_postal"] = input("Ingrese el nuevo código postal: ")
    cliente["codigo_empleado_rep_ventas"] = input("Ingrese el nuevo código de empleado de representante de ventas: ")
    cliente["limite_credito"] = input("Ingrese el nuevo límite de crédito: ")

    clienteActualizado = {**clienteExistente, **cliente}
    peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", json=clienteActualizado)

    if peticion.status_code == 200:
        return {"message": "Cliente actualizado correctamente"}
    else:
        print(peticion.status_code)
        return {"message": "Error al actualizar el cliente" }

if __name__ == "__main__":
    id_cliente = input("Ingrese el ID del cliente que desea actualizar: ")
    resultado = actualizarCliente(id_cliente)
    print(resultado)




def menu():
 while True:
    os.system("clear")
    print("""
    ___       __          _       _      __                 __                  __            __      __                    __             ___            __           
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /__     ____/ /___ _/ /_____  _____   ____/ /__     _____/ (_)__  ____  / /____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \__,_/\__,_/\__/\____/____/   \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/  
                                                                                                                                                                       



                                                    1. Agregar clientes
                                                    2. Eliminar clientes
                                                    3. Actualizar clientes
                                                    0. Atras


            """)
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postClientes(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif opcion == 2:
               idCliente = int(input("Ingrese la id del cliente: "))
               resultado = deleteCliente(idCliente)
               print("Cliente eliminado exitosamente")
               input("Presione una tecla para continuar: ")
              elif (opcion == 3):
                id_cliente = input("Ingrese el ID del cliente que desea actualizar: ")
                resultado = actualizarCliente(id_cliente)
                print(resultado)
                input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break