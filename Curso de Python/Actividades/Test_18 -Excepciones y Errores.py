## Manejo de Excepciones en Python
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Manejo de la excepción
    print("Error: División por cero no permitida.")

## Manejo de excepciones múltiples
try:
    numero = int(input("Ingrese un número entero: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Entrada no válida. Por favor ingrese un número entero.")
except ZeroDivisionError:
    print("Error: División por cero no permitida.")


## Jerarquia de excepciones
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)