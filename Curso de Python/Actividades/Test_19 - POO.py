## Creacion de clases en Python
class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método de la clase
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
print(persona1.saludar())

##-------------------------> Ejemplo Cuenta Bancaria <-------------------------##
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso: {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso: {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        return f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}"

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.mostrar_saldo())
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.mostrar_saldo())
cuenta.retirar(2000)  # Intento de retiro con fondos insuficientes

##-------------------------> Ejemplo Biblioteca <-------------------------##
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

class User:
    def __init__(self,nombre,user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self,libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print(f"El usuario '{self.nombre}' no tiene el libro '{libro.titulo}' prestado.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self,libro):
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")

    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        print(f"El usuario '{usuario.nombre}' ha sido registrado en la biblioteca.")

    def mostrar_libros_disponibles(self):
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros:
            if libro.disponible:
                print(f"- {libro.titulo} de {libro.autor}")

# Crear instancia de libro
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
# Crear instancia de usuario
usuario1 = User("Carlos", 1)
# Crear instancia de biblioteca
biblioteca = Biblioteca()
# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
# Registrar usuario en la biblioteca
biblioteca.registrar_usuario(usuario1)
# Mostrar libros disponibles
biblioteca.mostrar_libros_disponibles()
# Usuario presta un libro
usuario1.prestar_libro(libro1)
# Mostrar libros disponibles después del préstamo
biblioteca.mostrar_libros_disponibles()
# Usuario devuelve un libro
usuario1.devolver_libro(libro1)
# Mostrar libros disponibles después de la devolución
biblioteca.mostrar_libros_disponibles()