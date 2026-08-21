# COnjuntos: Coleccion no rodena de elementos unicos (NO duplicados)

motos = {"kawazaki","benelli","harley","royal","kawazaki"}
print(motos)
print(type(motos))
print(len(motos)) ## Los elementos duplicados solo se cuentan una vez

conjuntoMix = {11111, True, "Unicornio"} ##Pueden alojar variables de diferente tipo
print(type(conjuntoMix))

## Recorrido del conjunto
for item in conjuntoMix:
    print(item)

## ADD: Agregar un elemento
conjuntoMix.add(45.2)
print(conjuntoMix)

## UPDATE: Agregar mas de un elemento
actualizacion = {"Schumacher","Hamilton"}
conjuntoMix.update(actualizacion)
print(conjuntoMix)

## REMOVE: Eliminar un elemento especifico
conjuntoMix.remove(True)
print(conjuntoMix)

## DISCARD: Eliminar un elemento especifico
conjuntoMix.discard("Schumacher")
print(conjuntoMix)

## POP: Eliminar un elemento ALEATORIO
conjuntoMix.pop()
print(conjuntoMix)

##CLEAR: Limpiar un conjunto por completo
conjuntoMix.clear()
print(conjuntoMix)