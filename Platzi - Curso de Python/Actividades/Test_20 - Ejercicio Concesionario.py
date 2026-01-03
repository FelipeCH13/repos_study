##Creacion Clase Vehiculo
class Vehiculo:

    ## Metodo Constructor
    def __init__ (self, marca,modelo,anio,precio,condicion):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.condicion = condicion  # 'nuevo' o 'usado'
        self.disponible = True

    ## Consulta Información del vehículo
    def mostrar_info(self):
        info = f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}, Condición: {self.condicion}, Disponible: {self.disponible}"
        return info
    
    ## Vender el vehiculo
    def vender(self):
        if self.disponible == True:
            self.disponible = False
            print(f"El vehículo {self.marca} {self.modelo} ha sido vendido.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no está disponible para la venta.")

    #---------------Metodos Polimorfismo---------------#
    def encender(self):
        raise NotImplementedError("La clase hija debe implementar este método")
    def apagar(self):
        raise NotImplementedError("La clase hija debe implementar este método")

class Auto(Vehiculo):
    def encender(self):
        if not self.disponible:
            return f"El auto {self.marca} {self.modelo} no está disponible."
        else:
            return f"El auto {self.marca} {self.modelo} está encendido."

    def apagar(self):
        if not self.disponible:
            return f"El auto {self.marca} {self.modelo} no está disponible."
        else:
            return f"El auto {self.marca} {self.modelo} está apagado."

class Moto(Vehiculo):
    def encender(self):
        if not self.disponible:
            return f"La moto {self.marca} {self.modelo} no está disponible."
        else:
            return f"La moto {self.marca} {self.modelo} está encendida."

    def apagar(self):
        if not self.disponible:
            return f"La moto {self.marca} {self.modelo} no está disponible."
        else:
            return f"La moto {self.marca} {self.modelo} está apagada."

class bicicleta(Vehiculo):
    def encender(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} {self.modelo} no está disponible."
        else:
            return f"La bicicleta {self.marca} {self.modelo} está lista para usar."

    def apagar(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} {self.modelo} no está disponible."
        else:
            return f"La bicicleta {self.marca} {self.modelo} ha sido guardada."

class camion(Vehiculo):
    def encender(self):
        if not self.disponible:
            return f"El camión {self.marca} {self.modelo} no está disponible."
        else:
            return f"El camión {self.marca} {self.modelo} está encendido."

    def apagar(self):
        if not self.disponible:
            return f"El camión {self.marca} {self.modelo} no está disponible."
        else:
            return f"El camión {self.marca} {self.modelo} está apagado."

## Creacion Clase Concesionario
class Concesionario:
    def __init__(self):
        self.vehiculos = []

    ## Agregar vehiculo al concesionario
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} agregado al concesionario.")

    ## Mostrar vehiculos disponibles
    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles en el concesionario:")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(vehiculo.mostrar_info())

    ## Vender un vehiculo
    def vender_vehiculo(self, vehiculo):
        vehiculo.vender()

## Creacion Clase Cliente
class Cliente:
    def __init__ (self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono

    def consultar_vehiculos(self, concesionario):
        concesionario.mostrar_vehiculos_disponibles()

    def comprar_vehiculo(self, concesionario, vehiculo):
        if vehiculo.disponible:
            concesionario.vender_vehiculo(vehiculo)
            print(f"Cliente {self.nombre} ha comprado el vehículo {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} no está disponible para la compra.")

# Ejemplo de uso
## Creacion del objeto Concesionario
concesionario = Concesionario()
## Cracion de objetos vehiculos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 20000, "nuevo")
vehiculo2 = Vehiculo("Honda", "Civic", 2018, 15000, "usado")
## vehiculos agregados al concesionario
concesionario.agregar_vehiculo(vehiculo1)
concesionario.agregar_vehiculo(vehiculo2)
## Instanciacion del cliente
cliente = Cliente("Juan Perez", "555-1234")
## Ejecucion de los metodos del cliente
cliente.consultar_vehiculos(concesionario)
cliente.comprar_vehiculo(concesionario, vehiculo1)
cliente.comprar_vehiculo(concesionario, vehiculo2)
cliente.consultar_vehiculos(concesionario)
