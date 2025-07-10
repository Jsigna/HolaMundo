#examen programacion ejercicio notebook

def menu_inicial():
    while True:
        print("\n*** MENU PRINCIPAL ***\n")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        opcion = input("Ingrese su opcion 1-4 : ")
        
        match opcion:
            case "1":
                marca = input("\nIngrese la marca del notebook que esta buscando : ").lower()
                stock_marca(marca)
            case "2":
                p_min = 0
                p_max =0
                try:
                    p_min = int(input("\nIngrese El precio minimo del articulo que desea buscar : \n"))
                    p_max = int(input("\nIngrese El precio maximo del articulo que desea buscar : \n"))
                except:
                    print("Ingrese un valor valido! que sea un numero!")    
                busqueda_precio(p_min,p_max)
            case "3":
                while True:

                    modelo = input("Ingrese el modelo del notebook que desea actualizar el precio : ")
                    for buscar_modelo in productos:
                        if buscar_modelo == modelo:
                            p = int(input("Ingrese el nuevo precio : "))
                            break
                        else:
                            print("Modelo incorrecto ingrese un modelo valido!")    
                    if zar_precio(modelo, p):
                        print("precio actualizado!")
                        confirmacion  = input("Desea actualizar otro precio de notebook?. si o no : ").lower()
                        if confirmacion == "si":
                            print("")
                        else:
                            print("adios")
                            break    
            case "4":
                print("Saliendo del programa , adioos")
                break
            case _:
                print("Ingrese una opcion valida entre 1 y 4! ") 
  
def stock_marca(marca):  
    cantidad_de_stock = 0
    for busqueda in productos:
        if productos[busqueda][0] == marca:
            cantidad_de_stock += stock[busqueda][1]
    print(f"\nLa cantidad de stock disponible para esta marca es {cantidad_de_stock}")  
                
def busqueda_precio(p_min,p_max):
    lista_mostrar = []
    for busqueda in stock:
        if stock[busqueda][0] in range(p_min,p_max+1) and stock[busqueda][1] > 0:
          lista_mostrar.append((productos[busqueda][0],busqueda))
    if len(lista_mostrar) == 0:
        print("No hay notebook dentro del rango de precio")
    else:
        print(f"{lista_mostrar}")          
    
     
        
def zar_precio(modelo, p):
    for buscar in stock:
        if buscar == modelo:
            stock[buscar][0] = p
            break
    print(f"{stock[buscar][0]}")
    return True                             





productos = {'8475HD':['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD':['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD':['asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD':['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD':['asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD':['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD':['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD':['dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD':   [387990,10],
         '2175HD':   [327990,4],
         'JjfFHD':   [424990,1],
         'fgdxFHD':  [664990,21],
         '123FHD':   [290890,32],
         '342FHD':   [444990,7],
         'GF75HD':   [749990,0],
         'UWU131HD': [349990,1],
         
}

menu_inicial()