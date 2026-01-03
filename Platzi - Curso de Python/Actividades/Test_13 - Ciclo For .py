## Uso del ciclo for
nombres = ["Ana", "Luis", "Carlos", "Marta"]
# Iterar sobre la lista de nombres
for nombre in nombres:
    print("Hola", nombre)
print("Fin del ciclo for")
# Iterar sobre un rango de números
for i in range(5):
    print("Número:", i)
print("Fin del ciclo for con rango")

# Uso de Range con inicio y fin
for j in range(2, 10):
    print("Número:", j)    

#Uso de Range con inicio, fin y paso
for j in range(2, 10, 2):
    print("Número par:", j)

## Uso de for e if
for numero in range(10):
    if numero % 2 == 0:
        print(numero, "es un número par")
    else:
        print(numero, "es un número impar")

## Uso de while
contador = 1
## Ciclo  hasta que el contador sea menor que 16
while contador < 16:
    if contador % 2 == 0:
        print(contador, "es un número par")
    else:
        print(contador, "es un número impar")
    # Incremento del contador
    contador += 1

## Uso de break y continue
for numero in range(20):
    if numero == 17:
        print("Se encontró el número 17, saliendo del ciclo")
        break  # Sale del ciclo cuando encuentra el número 17
    if numero % 2 == 0:
        continue  # Salta a la siguiente iteración si el número es par
    print(numero, "es un número impar menor que 17")