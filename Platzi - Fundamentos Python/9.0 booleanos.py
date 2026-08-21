v = True
f = False

print(v)  # Imprime True
print(f)  # Imprime False

print(12451 > 100)  # Imprime True porque 12451 es mayor que 100
print(12451 < 100)  # Imprime False porque 12451 no es menor que 100

print(type(v))  # Imprime <class 'bool'> porque v es un valor booleano

print(bool(1))  # Imprime True porque 1 se considera verdadero
print(bool(0))  # Imprime False porque 0 se considera falso

print(bool("Hola"))  # Imprime True porque una cadena no vacía se considera verdadera
print(bool(""))  # Imprime False porque una cadena vacía se considera falsa
print(bool(0.0))  # Imprime False porque 0.0 se considera falso
print(bool([]))  # Imprime False porque una lista vacía se considera falsa

x = 3.14
print(isinstance(v, bool))  # Imprime True porque v es una instancia de la clase bool
print(isinstance(x, bool))  # Imprime True porque f es una instancia de la clase bool