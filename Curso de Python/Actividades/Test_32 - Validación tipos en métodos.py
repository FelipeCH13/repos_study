def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("El primer argumento debe ser un número (int o float).")
        return None
    if b == 0:
        print("Error: División por cero no permitida.")
        return None
    
    return a / b

# Pruebas de la función con diferentes tipos de argumentos
resultado1 = divide(10, 2)
resultado = divide(10, 0)