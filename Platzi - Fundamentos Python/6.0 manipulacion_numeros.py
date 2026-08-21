x = 3
y = 33.3
z = 1j

print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex

positivo = 42
negativo = -42
imaginario = 1j - 5

positivo_float = float(positivo)  # Convertir un número entero a un número decimal
print(positivo_float)  # 42.0
print(type(positivo_float))  # float

y_int = int(y)  # Convertir un número decimal a un número entero
print(y_int)  # 33
print(type(y_int))  # int

entero_complejo = complex(x)  # Convertir un número entero a un número complejo
float_complejo = complex(y)  # Convertir un número decimal a un número complejo
print(entero_complejo)  # 3 + 0j
print(type(entero_complejo))  # complex
print(float_complejo)  # 33.3 + 0j
print(type(float_complejo))  # complex

import random
aleatorio = random.randint(1, 100)  # Genera un número entero aleatorio entre 1 y 100
print(aleatorio)

aleatorio_float = random.uniform(1.0, 100.0)  # Genera un número decimal aleatorio entre 1.0 y 100.0
print(aleatorio_float)

aleatorio_complejo = complex(random.uniform(1.0, 100.0), random.uniform(1.0, 100.0))  # Genera un número complejo aleatorio
print(aleatorio_complejo)
