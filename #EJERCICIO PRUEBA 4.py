#EJERCICIO PRUEBA 4

def menu_inicial():
  while True:
    print("\n___TOTEM AUTOATENCIÓN RESERVA STRIKE___\n")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas.")
    print("3.- Ver stock de reservas.")
    print("4.- Salir.")
    
    opcion = input("ingrese su opcion : ")
    
    match opcion:
      case "1":
        reserva_completa()
      case "2":
        buscar_reservas()
      case "3":
        buscar_cupos()
      case "4":
        print("Saliendo del programa chaitoo ")  
        break  
      case _:
        print("\nIngrese una opcion valida!! entre 1 y 4 ") 

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
      confirmacion = input("para confirmar la reserva escriba su frase secreta : ")
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
                          "tipo" : "estandar",
                          "n_reserva" : 1
   }
  reservas.append(reserva_diccionario)

  
def buscar_reservas():
  
  while True:
    busqueda_nombre = input("Ingrese el nombre de la reserva que desea buscar : ")
    nombre_encontrado = False
    for busqueda_reservas in reservas:
      if busqueda_reservas["nombre"] == busqueda_nombre:
        nombre_encontrado = True
        print(f"Reserva encontrada : {busqueda_nombre}-{busqueda_reservas['n_reserva']} par(es) ({busqueda_reservas['tipo']})")
        if busqueda_reservas["n_reserva"] < 2:
          confirmacion = input("Desea reservar otro par? para confirmar escriba 'si' , lo contrario 'no' : ").lower()
          if confirmacion == "si":
            print("se reservara otro par para usted!")
            busqueda_reservas["tipo"] = "vip"
            busqueda_reservas["n_reserva"] = 2
            break
          elif confirmacion == "no":
            print("adioos")
            break
        else:
          print("ha llegado a su limite de reservas que es maximo 2!")
    if not nombre_encontrado:
      print("no se encuentra su reserva ")
      break
    else:
      break    

def buscar_cupos():
  contador_reservas = 0
  for i in reservas:
    contador_reservas += i["n_reserva"]
  print(f"La cantidad de reservas son {contador_reservas}")  
  print(f"la cantidad de cupos disponibles son {20 - contador_reservas}")

    

reservas = []
menu_inicial()

