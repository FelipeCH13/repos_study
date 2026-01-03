## Uso de operadore númericos
x=342
y=7631
print("Suma: ", x + y)
print("Resta: ", x - y)
print("Multiplicacion: ", x * y)
print("Potencia: ", x ** 2 )
print("División: ", x / y)
print("Parte Entera de la División: ", y // x)
print("Modulo: ", x % y)

## ---------------Shortcuts
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)

## Uso de PEMDAS
operation = 12 + 5 * 2
print(operation)
operation_pemdas = 12 + (5 * 2)
print(operation_pemdas)
operation_pemdas_2 = (12 + 5) * 2
print(operation_pemdas_2)

operation_pemdas_3 = (2+3) * (4**2)/ 8-1
## ----------------------> De izquierda a derecha, en este caso lo ultimo que se realizo fue la sustraccion dado el orden de PEMDAS
print(operation_pemdas_3)