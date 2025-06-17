#ejercicio prueba 1
n_personas= 0
print("esquema de vacunaciones")
try:
  n_personas = int(input("ingrese el numero de personas a registrar : "))
except:
  print("Ingrese un numero valido")  
e_completo = 0
e_incompleto = 0
aux = 0

for i in range(n_personas):
  while True:
    aux = 0
    num_vacunas = 0
    try:
      num_vacunas = int(input("Ingrese el numero de vacunas para cada persona (1 persona cada vez) : "))
    except:
      print("Ingrese un numero valido")  
    if num_vacunas == 3:
        e_completo+= 1
        aux+= 1
        print("Esquema Completo ")
    elif 3< num_vacunas > 3:
        e_incompleto+= 1
        aux+= 1
        print("Esquema Incompleto ")
    else:
      print("conteo fallido")    
    if aux > 0 :
      break     
  
print(f"Se registraron {e_completo} personas con esquema completo")
print(f"Se registraron {e_incompleto} personas con esquema incompleto")    
    