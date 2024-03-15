# from tabulate import tabulate
import modules.getEmpleados as empleado
import modules.getClients as clientes
import modules.getPedidos as pedidos
import modules.getPagos as pagos
import modules.getOficina as oficina
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto
import os
import re



# print(tabulate(empleado.getAllNombreApellidoEmailJefe(7)))
# print(clientes.getAllNombrePais("Spain"))

# print(tabulate(producto.getAllStocksPriceGama)("Ornamentales", 100), headers="keys", tablefmt="github")

def menuProducto():
   while True:
      print("""

    ____  _                            _     __               __                                     __                             __           __            
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                                                                          /_/                                                  

                          1. Reporte de los productos
                          2. Guardar, Actualizar y Eliminar productos
                          0. Regresar al menu principal

                        """)
      opcion = input("\nSeleccione una de las opciones: ")
      if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Repproducto.menu()
            if(opcion == 2):
              CRUDproducto.menu()
            elif(opcion == 0):
              break





if(__name__ == "__main__"):
    while True:
        os.system("clear")
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

        option = input("\nSeleccione una de las opciones: ")
        if(re.match(r'[0-9]+$', option) is not None):
         option = int(option)
         if(option>=0 and option<=6):
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
             menuProducto()
           elif(option == 0):
            break
