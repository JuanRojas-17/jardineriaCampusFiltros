import json
import requests
import os
from tabulate import tabulate
import re
import modules.getPagos as gPa

def conexionPagosjson():
      peticion=requests.get("http://154.38.171.54:5006/pagos") 
      Informacion=peticion.json()  
      return Informacion  

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

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5006/pagos",headers=headers, data=json.dumps(pago, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]

if __name__ == "__main__":
    postPago()

def deletePago(id):
    data = gPa.getPagoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Pago eliminado correctamete"})
            return{
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"Pago no encontrado",
                "id": id
            }],
            "status": 400,
        }
    
def actualizarpago(id):
    pagoExistente = gPa.getPagoCodigo(id)
    print(pagoExistente)
    if len(pagoExistente) == 0:
        return {"message": "pago no encontrado"}

    pago = {}
    
    print("Ingrese los nuevos datos del pago:")
    
    pago["codigo_pago"] = input("Ingrese el nuevo código del pago: ")
    pago["nombre"] = input("Ingrese el nuevo nombre del pago: ")
    pago["gama"] = input("Ingrese la nueva gama del pago: ")
    pago["dimensiones"] = input("Ingrese las nuevas dimensiones del pago: ")
    pago["proveedor"] = input("Ingrese el nuevo proveedor del pago: ")
    pago["descripcion"] = input("Ingrese la nueva descripción del pago: ")
    pago["cantidadEnStock"] = int(input("Ingrese la nueva cantidad en stock del pago: "))
    pago["precio_venta"] = float(input("Ingrese el nuevo precio de venta del pago: "))
    pago["precio_proveedor"] = float(input("Ingrese el nuevo precio proveedor del pago: "))

    pagoActualizado = {**pagoExistente, **pago}
    peticion = requests.put(f"http://154.38.171.54:5008/pagos/{id}", json=pagoActualizado)

    if peticion.status_code == 200:
        return {"message": "pago actualizado correctamente"}
    else:
        print(peticion.status_code)
        return {"message": "Error al actualizar el pago" }

if __name__ == "__main__":
    id_pago = input("Ingrese el ID del pago que desea actualizar: ")
    resultado = actualizarpago(id_pago)
    print(resultado)

def menu():
 while True:
    print("""
    ___       __          _       _      __                 __                  __      __                    __                                    
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ _____/ /___  _____   ____/ /___ _/ /_____  _____   ____/ /__     ____  ____ _____ _____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __  / __ \/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__,_/\____/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/\__,_/\__, /\____/____/  
                                                                                                                   /_/          /____/              
  

                                                            1. Agregar pagos
                                                            2. Eliminar pagos
                                                            3. Actualizar pagos
                                                            0. Regresar





""")   
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
              if(opcion == 1):
               print(tabulate(postPago(), headers="keys", tablefmt="github"))
               input("Presione una tecla para continuar: ")
              elif(opcion == 2):
               idpago = int(input("Ingrese la id del pago: "))
               resultado = deletePago(idpago)
               print("pago eliminado exitosamente")
               input("Presione una tecla para continuar: ")
              elif (opcion == 3):
                id_pago = input("Ingrese el ID del pago que desea actualizar: ")
                resultado = actualizarpago(id_pago)
                print(resultado)
                input("Presione una tecla para continuar: ")
              elif(opcion == 0):
               break