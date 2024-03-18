# from tabulate import tabulate
import modules.getEmpleados as empleado
import modules.getClients as clientes
import modules.getPedidos as pedidos
import modules.getPagos as pagos
import modules.getOficina as oficina
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto
import modules.postPagos as CRUDpagos
import modules.getPagos as Reppagos
import modules.getPedidos as Reppedidos
import modules.postPedidos as CRUDpedidos
import modules.getOficina as Repoficina
import modules.postOficina as CRUDoficina
import modules.getEmpleados as Repempleados
import modules.postEmpleados as CRUDempleados
import modules.getClients as Repclientes
import modules.postClients as CRUDclientes
import modules.getGamas as Repgamas
import modules.postGamas as CRUDgamas
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

def menuPago():
   while True:
      print("""
    ____  _                            _     __               __                                     __                                    
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     ____  ____ _____ _____  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/\__,_/\__, /\____/____/  
                                                                                                          /_/          /____/              
  

                          1. Reporte de los pagos
                          2. Guardar, Actualizar y Eliminar pagos
                          0. Regresar al menu principal

                        """)
      opcion = input("\nSeleccione una de las opciones: ")
      if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Reppagos.menu()
            if(opcion == 2):
              CRUDpagos.menu()
            elif(opcion == 0):
              break

def menuPedidos():
  while True:
    print("""

    ____  _                            _     __               __                                     __                       ___     __          
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     ____  ___  ____/ (_)___/ /___  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ _ \/ __  / / __  / __ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/\___/\__,_/_/\__,_/\____/____/  
                                                                                                          /_/                                     

          
                                    1. Reporte de los pedidos
                                    2. Guardar, Actualizar y Eliminar pedidos
                                    0. Regresar al menu principal
""")
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Reppedidos.menu()
            if(opcion == 2):
              CRUDpedidos.menu()
            elif(opcion == 0):
              break

def menuOficina():
  while True:
    print("""

    ____  _                            _     __               __                                     __              _____      _                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     ____  / __(_)____(_)___  ____ ______
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  


                                              1. Reporte de las oficinas
                                              2. Guardar, Actualizar y Eliminar oficinas
                                              0. Regresar al menu principal                                                                                                                          

""")
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Repoficina.menu()
            if(opcion == 2):
              CRUDoficina.menu()
            elif(opcion == 0):
              break

def menuEmpleados():
  while True:
    print("""
    ____  _                            _     __               __                                     __                             __               __          
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                                                                                         /_/                                     


                                              1. Reporte de los empleados
                                              2. Guardar, Actualizar y Eliminar empleados
                                              0. Regresar al menu principal                                                                                                                          

""")
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Repempleados.menu()
            if(opcion == 2):
              CRUDempleados.menu()
            elif(opcion == 0):
              break

def menuCliente():
  while True:
    print("""
    ____  _                            _     __               __                                     __             ___            __           
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     _____/ (_)__  ____  / /____  _____
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/  
                                                                                                                                                



                                              1. Reporte de los clientes
                                              2. Guardar, Actualizar y Eliminar clientes
                                              0. Regresar al menu principal                                                                                                                          

""")
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Repclientes.menu()
            if(opcion == 2):
              CRUDclientes.menu()
            elif(opcion == 0):
              break

def menuGamas():
  while True:
    print("""

    ____  _                            _     __               __                                     __                                        
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__     ____ _____ _____ ___  ____ ______
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ `/ __ `/ __ `__ \/ __ `/ ___/
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /_/ / / / / / / /_/ (__  ) 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \__, /\__,_/_/ /_/ /_/\__,_/____/  
                                                                                                           /____/                              


                                              1. Reporte de las gamas
                                              2. Guardar, Actualizar y Eliminar gamas
                                              0. Regresar al menu principal                                                                                                                          

""")
    opcion = input("\nSeleccione una de las opciones: ")
    if(re.match(r'[0-9]+$', opcion) is not None):
         opcion = int(opcion)
         if(opcion>=0 and opcion<=6):
            if(opcion == 1):
              Repgamas.menu()
            if(opcion == 2):
              CRUDgamas.menu()
            elif(opcion == 0):
              break

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
                          7. Gamas
                          0. Salir

""")

        option = input("\nSeleccione una de las opciones: ")
        if(re.match(r'[0-9]+$', option) is not None):
         option = int(option)
         if(option>=0 and option<=7):
           if(option == 1):
            menuCliente()
           elif(option == 2):
            menuOficina()
           elif(option == 3):
             menuEmpleados()
           elif(option == 4):
              menuPedidos()
           elif(option ==5):
             menuPago()
           elif(option == 6):
             menuProducto()
           elif(option == 7):
             menuGamas()
           elif(option == 0):
            break
