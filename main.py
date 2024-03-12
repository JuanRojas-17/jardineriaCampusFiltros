from tabulate import tabulate

import os
import modules.getEmpleados as empleado
import modules.getClients as clientes
import modules.getPedidos as pedidos
import modules.getPagos as pagos
import modules.getOficina as oficina
import modules.getProducto as productos

# print(tabulate(empleado.getAllNombreApellidoEmailJefe(7)))
# print(clientes.getAllNombrePais("Spain"))

# print(tabulate(producto.getAllStocksPriceGama)("Ornamentales", 100), headers="keys", tablefmt="github")

if(__name__ == "__main__"):
    while True:
        print("""
        
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
        

                          1. Clientes
                          2. Oficinas
                          3. Empleados
                          4. Pedidos
                          5. Pagos
                          6. Productos
                          0. Salir

""")
        option = int(input("\nSeleccione una de las opciones: "))
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
        elif(option == 6):
           productos.menu()
        if(option == 0):
          break