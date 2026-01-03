## Ejemplo de comentarios y docstrings en Python
def suma(a, b):
    """
    Esta función recibe dos números y devuelve su suma.

    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.

    Retorna:
    int, float: La suma de los dos números.
    """
    return a + b
# Uso de la función suma
resultado = suma(5, 3)
print("La suma es:", resultado) # Salida: La suma es: 8
# Comentario de una sola línea explicando el siguiente bloque de código