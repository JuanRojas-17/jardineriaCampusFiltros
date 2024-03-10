
from tabulate import tabulate

import os
import modules.getEmpleados as empleado
import modules.getClients as clientes
import modules.getPedidos as pedidos
import modules.getPagos as pagos
import modules.getOficina as oficina

# print(tabulate(empleado.getAllNombreApellidoEmailJefe(7)))
# print(clientes.getAllNombrePais("Spain"))

if(__name__ == "__main__"):
         os.system("clear")
         print("""
        
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
        

                          1. Cliente
                          2. Oficina
                          3. Empleado
                          4. Pedidos
                          5. Pago

""")
try:
   option = int(input("\nSeleccione una de las opciones: "))
except ValueError:
   print("Opcion incorrecta")
else:
   if(option == 1):
      clientes.menu()
   elif(option == 2):
       oficina.menu()
   elif(option == 3):
       empleado.menu()
   elif(option == 4):
       pedidos.menu()
   elif(option ==5):
       pagos.menu()