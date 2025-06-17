#ejercicio 2
numeros = []
while True:
  opcion = 0
  print("\n*** MENU PRINCIPAL ***")
  print("1.- Ingresar número.")
  print("2.- Mostrar mayor.")
  print("3.- Mostrar promedio.")
  print("4.- Salir.")
  try:
    opcion = int(input("Ingrese su opcion del 1 al 4 : "))
  except:
      print("ingrese una opcion valida 1-4 ")
      
  if opcion == 1:
    while True:
        numeros = int(input("ingrese un numero entre 0 y 100 : "))
        if numeros >= 0 and numeros <= 100:
          print("ingreso exitoso ")
        else:
          print("ingrese un numero valido") 
        pregunta = input("Quieres agregar otro numero? si o no")  
        if pregunta == "no":
          break
        print(numeros)
           
          

        
  if opcion == 2:
    print()
    
  if opcion == 3:
    print()
    
  if opcion == 4:
    ("saliendo del programa")
    break
      
          
        
    
  
     
  
  