from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        mostrar_menu()
        opcion = input("Bienvenido a Cafesito! Por favor selecciona una opcion!")
        
        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por haber utilizado nuestro servicio")
            break
        else:
            print("\n Opcion invalida, por favor indique alguna de las opciones sugeridas")
            
if __name__=="__main__":
    main()