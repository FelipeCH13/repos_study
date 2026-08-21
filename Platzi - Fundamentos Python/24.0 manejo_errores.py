try:
    print("Intento de ejecucion")
    numero = 10 / 0
except ZeroDivisionError: ## Acompañado del tipo de error
    print("Captura del error")
    
try:
    print(x)
except NameError:
    print("La variable utilizada no ha sido declarada.")
finally:
    print("Esto se ejecutara sea exitoso el bloque o no.")