## Coleccion de pares clave valor

motos = {
    "marca":"Kawazaki",
    "modelo":"Z900",
    "año":"2025"
}

print(motos)

## Seleccionar un valor de acuerdo a su clave
print(motos["marca"])
## Seleccionar un valor de acuerdo a su clave con el metodo get( )
print(motos.get("marca"))

## Obtener las Keys en el diccionario
print(motos.keys())

## Obtener los valores en el diccionario
print(motos.values())

## Uso del In para validar la existencia de un elemento
if "marca" in motos:
    print("Marca es una de las propiedades del diccionario de Motos")

## Modificar valores de un elemento
motos["año"] = 2014
print(motos)
## Agregar valores al diccionario
motos["cilindraje"] = 900
print(motos)

##Uso del Update - Modificar
motos.update({"cilindraje":950})
print(motos)

##Uso del Update - Agregar y modificar en un solo comando
motos.update({"año":2021, "color":"azul"})
print(motos)

## Recorrer las claves del diccionario
for clave in motos:
    print(clave)

for value in motos.values():
    print(value)
    
for k,v in motos.items():
    print(k,v)
    
    
## DICCIONARIOS ANIDADOS
familia = {
    "hijo_1":{
        "nombre":"Juan",
        "edad":20
    },
    "hijo_2":{
        "nombre":"Pedro",
        "edad":15
    },
    "hijo_3":{
        "nombre":"Ana",
        "edad":18
    }
}
##Lectura de diccionarios anidados
print(familia["hijo_1"]["nombre"])

# ## Eliminar elementos
# motos.pop("color")
# print(motos) 

# ## Eliminar el ultimo elemento
# motos.popitem()
# print(motos)

# motos.clear()
# print(motos)