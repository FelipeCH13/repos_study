## Operadores de asignacion

x = 55
print('Asignacion:',x)
x += 3
print('Asignacion con suma:',x)
x -= 3
print('Asignacion con resta:',x)
x *= 5
print('Asignacion con multiplicacion:',x)
x /= 5
print('Asignacion con division:',x)
x %= 5
print('Asignacion con modulo:',x)

y = 55
y //= 5
print('Asignacion con division entera:',y)
y **= 2
print('Asignacion con exponente:',y)

## Walrus (morsa) - Posibilidad de asignar una variable dentro de un metodo
print(z := 3)
print(z)
