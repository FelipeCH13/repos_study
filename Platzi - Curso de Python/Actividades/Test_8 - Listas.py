## Uso de listas, se utilizan corchetes
sitios_viaje = ["Miami", "Manizales", "Pereira", "Bucaramanga", "Sidney"]
print(sitios_viaje)
print(type(sitios_viaje))

## Puede contener cualquier tipo de variable
no_olvidar = ["Contraseña",12,3.14, True, [1,2,3]]
print(no_olvidar)

## Tamaño de la lista
print(len(no_olvidar))
print("Contraseña: ",no_olvidar[0])

## Intervalo de datos o informacion
print("No Olvidar: ",no_olvidar[0:2])
print("No Olvidar: ",no_olvidar[:4]) ## Buena practica dejar el inicio o final vacio

##Metodos de las listas
no_olvidar.append("Password")
print(no_olvidar)

## Insertar en una posicion especifica
no_olvidar.insert(2,"Se me olvido")
print(no_olvidar)

## Contar elementos en la lista
print(no_olvidar.index("Contraseña"))

## Listas con numeros
numbers = [1,544,76554,863,12]
print(numbers)
## Valores maximos y minimos
print(max(numbers))
print(min(numbers))

## Eliminar elementos de la lista
del no_olvidar[0]
print(no_olvidar)

## Eliminar toda la lista
## del no_olvidar
## print(no_olvidar)

## Precauciones al copiar las listas
numbers2 = numbers
print(numbers2)
print(numbers)

## Eliminar el primer elemento de la lista numbers2
del numbers2[0]
## Afecta a las dos listas
print(numbers2)
print(numbers)

## Ambas tienen la misma direccion de memoria
print(id(numbers))
print(id(numbers2))

## Forma correcta de copiar una lista
numbers3 = numbers[:]
del numbers3[0]
print(numbers3)
## No afecta a la lista original
print(id(numbers3))