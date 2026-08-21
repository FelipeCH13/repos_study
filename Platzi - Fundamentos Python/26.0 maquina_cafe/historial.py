ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\n Este es el historial de Pedidos")
        with open(ARCHIVO_PEDIDOS,"r",encoding = "utf-8") as archivo:
            pedidos = archivo.readlines()

            if pedidos:
                for i, pedido in enumerate(pedidos, start=1): 
                    print(str(i) + ". " + pedido.strip())
            else:
                print("Aun no hay ningun pedido.")
    except FileNotFoundError:
        print("\n No contamos con un historial de pedidos")