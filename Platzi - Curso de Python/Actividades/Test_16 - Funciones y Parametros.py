## Uso de funciones
## La funcion va a solicitar el parametro del nombre
from turtle import clear


def saludar():
    """Función que saluda a una persona por su nombre."""
    nombre = input("Por favor, introduce tu nombre: ")
    mensaje = f"Hola, {nombre}! Bienvenido."
    return mensaje
print(saludar()) 


## Ejemplo de funcion con parametros
def saludar_persona(nombre):
    """Función que saluda a una persona por su nombre."""
    mensaje = f"Hola, {nombre}! Bienvenido."
    return mensaje
print(saludar_persona("Carlos"))
print(saludar_persona("Ana"))

## Ejemplo de funciones para una calculadora
def sumar(a, b):
    """Función que suma dos números."""
    return a + b

def restar(a, b):
    """Función que resta dos números."""
    return a - b

def multiplicar(a, b):
    """Función que multiplica dos números."""
    return a * b

def dividir(a, b):
    """Función que divide dos números."""
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

## Selecciona la funcion a utilizar

while True:
    print("Calculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    input_usuario = input("Selecciona la operación (1-5): ")

    while input_usuario not in ["1", "2", "3", "4", "5"]:
        print("Operación no válida. Inténtalo de nuevo.")
        input_usuario = input("Selecciona la operación (1-5): ")

    if input_usuario == "5":
        print("Saliendo de la calculadora.")
        break

    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Entrada no válida. Introduce números.")
        continue

    if input_usuario == "1":
        print(f"Resultado: {sumar(num1, num2)}")
    elif input_usuario == "2":
        print(f"Resultado: {restar(num1, num2)}")
    elif input_usuario == "3":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif input_usuario == "4":
        print(f"Resultado: {dividir(num1, num2)}")


## Uso de funciones lambda
## Funcion lambda para sumar dos numeros
sumar_lambda = lambda x, y: x + y
print(sumar_lambda(5, 3))
## Funcion lambda para elevar al cuadrado
cuadrado = lambda x: x ** 2
print(cuadrado(4))
## Funcion lambda para verificar si un numero es par
es_par = lambda x: x % 2 == 0
print(es_par(10))
print(es_par(7))