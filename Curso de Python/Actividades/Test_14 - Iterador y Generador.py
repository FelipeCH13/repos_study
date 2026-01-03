## Uso de iteradores
nombres = ["Ana", "Luis", "Carlos", "Marta"]
iterador = iter(nombres)
print(next(iterador))  # Imprime "Ana"
print(next(iterador))  # Imprime "Luis"
print(next(iterador))  # Imprime "Carlos"
print(next(iterador))  # Imprime "Marta"

## Iterador en un texto con un ciclo for
texto = "Hola"
for caracter in texto:
    print(caracter)

## Uso de generadores, se utilizan con la palabra clave yield
def generador_numeros():
    yield 1
    yield 2
    yield 3

for i in generador_numeros():
    print(i * i)  # Genera el cuadrado de i

## Serie de Fibonacci con generador
def fibonacci(limit):
    ## Inicializacion de los dos primeros numeros
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)  # Imprime los números de Fibonacci menores que 10