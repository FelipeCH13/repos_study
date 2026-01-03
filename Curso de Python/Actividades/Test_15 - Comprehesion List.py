## Comprehension List
## Listar el cuadrado de los numeros del 1 al 10
cuadrados = [x**2 for x in range(1,11)]
print(cuadrados)

## Listar el cubo de los números del 1 al 10
cubos = [x**3 for x in range(1,11)]
print(cubos)

## Listar los numeros pares del 1 al 20
pares = [x for x in range(1,21) if x%2==0]
print(pares)

## Convertir grados Celsius a Fahrenheit
celsius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

## Transponer una matriz 3x3
## Crear una matriz 3x3
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
## Transponer la matriz usando comprehension list
## transpuesta = [list(fila) for fila in zip(*matriz)
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(transpuesta)


## Ejercicios, sin ayuda de copilot
## Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
numeros = [1, 2, 3, 4, 5]
doble_numero = [x*2 for x in numeros]
print(doble_numero)

## Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_mayuscula = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print(palabras_mayuscula)

## Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]
diccionario = {claves[i]: valores[i] for i in range(len(claves))}
print(diccionario)

## Extraer Información de una Lista de Diccionarios Dada una lista de diccionarios que representan personas:
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
## crea una nueva lista con los nombres de las personas que viven en "Madrid" y tienen más de 30 años.
nombres_madrid_mayores_30 = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print(nombres_madrid_mayores_30)