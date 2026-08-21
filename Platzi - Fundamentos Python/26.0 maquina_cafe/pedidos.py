ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Por favor selecciona el cafe de tu preferencia:")
    print("1. Espresso")
    print("2. Latte")
    print("3. Americano")
    
    opcion = input("Ingresa la opción:")
    
    diccionario_cafes = {
        "1":"Espresso",
        "2":"Latte",
        "3":"Americano"
    }
    
    if opcion in diccionario_cafes:
        cafe_elegido = diccionario_cafes[opcion]
        print(f"Has seleccionado un {cafe_elegido}, buena eleccion!")
        
        with open(ARCHIVO_PEDIDOS,"a", encoding = "utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("La opcion no es valida, intenta de nuevo")
