import storage.pago as pa
from datetime import datetime
from tabulate import tabulate
import os
import re

def getAllPagos2008Paypal():
    pagos2008Paypal = []
    for val in pa.pago:
        fecha1 = val.get("fecha_pago")
        if val.get("forma_pago") == "PayPal" and fecha1.startswith("2008"):
            pagos2008Paypal.append(val)
    return pagos2008Paypal

def getAllTiposDePagos():
    tiposDePago = set()
    for val in pa.pago:
        tipos = val.get("forma_pago")
        if tipos not in tiposDePago:
            tiposDePago.add(tipos)
    return tiposDePago

def menu():
 while True:
    print("""
        
    ____                        __              __        __                                          
   / __ \___  ____  ____  _____/ /____     ____/ /__     / /___  _____   ____  ____ _____ _____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / / __ \/ ___/  / __ \/ __ `/ __ `/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  / / /_/ (__  )  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/  /_/\____/____/  / .___/\__,_/\__, /\____/____/  
          /_/                                                        /_/          /____/              

        

                            1. Pagos durante 2008 mediante PayPal
                            2. Informacion formas de pago
                            0. Regresar

""")
    
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
                print(tabulate(getAllPagos2008Paypal(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getAllTiposDePagos(), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break