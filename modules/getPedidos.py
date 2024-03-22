import json
import requests
from datetime import datetime
from tabulate import tabulate
import re

def dataPedidos():
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = peticion.json()
    return data

def getPedidoCodigo(id):
        peticion = requests.get(f"http://154.38.171.54:5007/pedidos/{id}")
        return(peticion.json()) if peticion.ok else []

def getAllEstadoPedidos():
    estadoPedidos = []
    data = dataPedidos()
    for val in data:
        estadoPedidos.append({
            "estado": val.get("estado"),
            "codigo_pedido": val.get("codigo_pedido")
        })
    return estadoPedidos

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()

    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")

        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1]) 
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end =   datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if(diff.days < 0):
            pedidosEntregado.append({
                "código_de_pedido": val.get("codigo_pedido"),
                "código_de_cliente": val.get("codigo_cliente"),
                "fecha_esperada": val.get("fecha_esperada"),
                "fecha_de_entrega": val.get("fechaEntrega"),
                "dias_de_retraso": -(diff.days)
            })
            
    return pedidosEntregado

def getAllCodigoClienteFechaEsperaEntregaPedidos2Dias():
    pedidosEntregado = []
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()

    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")

        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1]) 
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end =   datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if(diff.days >= 2):
            pedidosEntregado.append({
                "código_de_pedido": val.get("codigo_pedido"),
                "código_de_cliente": val.get("codigo_cliente"),
                "fecha_esperada": val.get("fecha_esperada"),
                "fecha_de_entrega": val.get("fechaEntrega"),
            })
            
    return pedidosEntregado

def getAllPedidosRechazados2009():
    pedidosRechazados2009 = []
    data = dataPedidos()
    for val in data:
        fecha1 = val.get("fecha_esperada")
        if val.get("estado") == "Rechazado" and fecha1.startswith('2009'):
            pedidosRechazados2009.append(val)
    return pedidosRechazados2009

def getAllPedidosEntregadosEnero():
    EntregadosEnero = list()
    for val in dataPedidos():
        if (val.get("estado") == "Entregado" and val.get("fechaEntrega") != None):
            FechaEntregada = "/".join(val.get("fechaEntrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                EntregadosEnero.append(val)
    return EntregadosEnero

def menu():
   while True:
    print("""
    ____                        __              __        __                             ___     __          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   ____  ___  ____/ (_)___/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / __ \/ _ \/ __  / / __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/  / .___/\___/\__,_/_/\__,_/\____/____/  
          /_/                                                        /_/                                     

        

                            1. Informacion estado pedidos
                            2. Informacion pedidos atrasados
                            3. Informacion pedidos adelantados por 2 dias
                            4. Informacion pedidos rechazados en el 2009
                            5. Informacion pedidos entregados en Enero
                            0. Regresar

""")
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                print(tabulate(getAllEstadoPedidos(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                print(tabulate(getAllCodigoClienteFechaEsperaEntregaPedidos2Dias(), headers="keys", tablefmt="github"))
            elif(opcion == 4):
                print(tabulate(getAllPedidosRechazados2009(), headers="keys", tablefmt="github"))
            elif(opcion == 5):
                print(tabulate(getAllPedidosEntregadosEnero(), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break