#EJERCICIO PRUEBA 4

def menu_inicial():
  while True:
    print("\n___Menu_Inicial___\n")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas.")
    print("3.- Ver stock de reservas.")
    print("4.- Salir.")
    
    opcion = input("ingrese su opcion : ")
    
    match opcion:
      case "1":
        reserva_completa()
      case "2":
        reserva_vip()
      case "3":
        buscar_cupos()
      case "4":
        print("Saliendo del programa chaitoo ")  
        break  
      case _:
        print("Ingrese una opcion valida!! entre 1 y 4 ") 

def validacion():
  salir_while = True
  while salir_while:
    aux = True
    nombre = input("Ingrese su nombre de usario : ")
    for copia in reservas:
      if copia["nombre"] == nombre:
        print("ingrese otro nombre , este ya esta ingresado!")
        aux = False
    if aux:
      print("Reserva casi lista!")
      confirmacion = input("para confirmar la reverva escribe textualmente lo que esta dentro de las comillas ''EstoyEnListaDeReserva'' : ")
      if confirmacion == "EstoyEnListaDeReserva":
        print("reserva completada !!")
        salir_while = False
        break
      else:
        print("\nintente nuevamente!\n")
        
  return nombre      
      
        
def reserva_completa():
  nombre = validacion()
  reserva_diccionario = {"nombre" : nombre,
                          "reservado" : True
   }
  reservas.append(reserva_diccionario)
  
def buscar_reservas():
  
  while True:
    busqueda_nombre = input("Ingrese el nombre de la reserva que desea buscar : ")
    for busqueda_reservas in reservas:
      if busqueda_reservas["nombre"] == busqueda_nombre:
        print(busqueda_reservas)
        confirmacion = input("Desea reservar otro par? para confirmar escriba 'si' , lo contrario 'no' : ")
        if confirmacion == "si":
          print("se reservara otro par para usted!")
          nombre_vip = busqueda_nombre
          return nombre_vip
        elif confirmacion == "no":
          print("adioos")
          break
      else:
        print("no se encuentra su reserva ")
        
def reserva_vip():
  nombre_vip = buscar_reservas()
  reserva_diccionario_vip ={"nombre_vip" : nombre_vip,
                            "reservado" : True
                            
  }
  
  reservas.append(reserva_diccionario_vip)

def buscar_cupos():
  cantidad_reservados = len(reservas)
  cantidad_disponibles = (20 - len(reservas))
  print(f"La cantidad de pares reservados son {cantidad_reservados}")
  print(f"la cantidad de pares disponibles son {cantidad_disponibles}")
  
 

reservas = []
menu_inicial()
















