## Uso de diccionarios, se utilizan llaves
diccionario = {"nombre":"Juan","edad":30,"ciudad":"New York"}
print(diccionario)
print(type(diccionario))
## Acceder a un elemento del diccionario
print(diccionario["nombre"])
## Eliminar un elemento del diccionario
del diccionario["edad"]
print(diccionario)
## Agregar un elemento al diccionario
diccionario["profesion"] = "Desarrollador"
print(diccionario)


## Uso de metodos en diccionarios
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

## Ejemplo practico en una agenda de contactos
agenda = {
    "Juan": {"telefono": "123456789", "email": "juan@example.com"},
    "Maria": {"telefono": "987654321", "email": "maria@example.com"},
    "Pedro": {"telefono": "456789123", "email": "pedro@example.com"}
}
print(agenda)
print(agenda["Maria"]["email"])