## Uso de recursividad con factoriales
def factorial(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = 30
print(f"El factorial de {numero} es {factorial(numero)}")

## Uso de recursividad en la serie de Fibonacci
def fibonacci(n):
    """Genera el n-ésimo número de Fibonacci de forma recursiva."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero_fibonacci = 10
print(f"El número de Fibonacci en la posición {numero_fibonacci} es {fibonacci(numero_fibonacci)}")
