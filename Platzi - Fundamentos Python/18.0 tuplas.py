## TUPLAS: Colecciones inmutables
lenguajes = ("Python","Java", "Go", "JavaScript","Python")

print(lenguajes)
print(lenguajes[1]) ##Obtener una variable en especifico segun su indice

print(len(lenguajes)) ##Identificar el tamaño de la tupla

frutas = ("Manzana",) # Las tuplas con un solo valor deben finalizar con una coma al final
print(type(frutas))

tuplaMix = (11111, True, "Unicornio") ##Pueden alojar variables de diferente tipo
print(type(tuplaMix))

x, y, z = tuplaMix # Desempaquetar una tupla en multiples variables
print(x,y,z)

## Unir tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2
print(tupla3)

print(tuplaMix * 3) ## Multipiocar los valores de las tuplas

## Recorrer el contenido de una tupla
for item in tuplaMix:
    print(item)

tupla_a = ("Portugal","Panama","Cabo Verde")
lista_comodin = list(tupla_a)
lista_comodin [0] = "Españita"
lista_comodin.append("Inglaterra")
tupla_a = tuple(lista_comodin)
print(tupla_a)