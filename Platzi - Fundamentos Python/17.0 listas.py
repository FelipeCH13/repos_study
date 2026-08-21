# LISTAS: Colecciones ordenadas, modificables y que permiten valores duplicados

jugadores = ["Lamine","Pedri","Ferran", "Olmo"]


print(jugadores)
print(type(jugadores))
print(jugadores[1]) ## Se indica la posicion del valor que queremos obtener de la lista

## Modificar el valor en una variable en especifico
jugadores[1] = "Porro"
print(jugadores[1])

## Es posible asignar diferentes tipos de variables en una misma lista
jugadores[3] = 10
print(jugadores)

## Identificar el tamano de la lista
print(len(jugadores))

## Seleccionar los elementos de la lista que se desean obtener segun su indice
print(jugadores[0:2])

## Recorrer el contenido de una lista
for jugador in jugadores:
    print(jugador)

## Metodos de las Listas
vehiculos = ["Jaguar","Ferrari","Aston Martin", "Volvo"]
vehiculos.append("Renault") ## Incluir un nuevo valor dentro de la lista
print(vehiculos)
vehiculos.insert(0,"Maseratti") ##Incluir un nuevo valor en una posicion en especifico
print(vehiculos)
vehiculos.remove("Aston Martin") ##Retirar un valor en especifico
print(vehiculos)
vehiculos.pop(0) ##Retirar un valor de acuerdo con el indice de su posicion
print(vehiculos)
vehiculos.sort() ##Ordenar el contenido de las listas de forma descendente
print(vehiculos)
vehiculos.reverse() #Ordenar el contenido de las listas de forma ascendente
print(vehiculos)

## UNIR LISTAS
listaUno = [1,2,3,4]
listaDos = [5,6,7,8]

## Unir listas dentro de una nueva variable
listaTres = listaUno + listaDos
print(listaTres)

## Extender una lista previamente ya creada
listaUno.extend(listaDos)
print(listaUno)