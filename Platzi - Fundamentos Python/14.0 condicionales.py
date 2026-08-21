x = 55
y = 66
z = 10


if x > y or z < x:
    print("5 es mayor que 3")
elif x == y:
    print("5 es igual a 5")
else:
    print("Probando las condiciones de if")
    
# Ejemplo condicionales Strings
a = "Barcelona"
b = "Madrid"
c = "Barcelona"

if a == c:
    if a == b:
        print("a es igual c pero es distinto de b")
    else:
        print("Estoy saliendo por el else del if interno")
else: 
    print("a no es igual a c")
    
e = 10
f = 10

if e == f:
    pass