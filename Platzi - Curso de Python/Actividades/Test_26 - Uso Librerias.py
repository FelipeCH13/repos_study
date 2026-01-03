import os
import math
import random
import statistics
import csv

#---------------------------> Uso de libreria OS <---------------------------#
cwd = os.getcwd()
print("¿En donde estoy trabajando? ", cwd)

# Listar archivos en el directorio actual
archivos = os.listdir(cwd)
print("Archivos en el directorio actual:", archivos)

# Listar archivos en el directorio actual
archivos = [f for f in os.listdir('.') if f.endswith('.py')]
print("Archivos .py en el directorio actual:", archivos)

#---------------------------> Uso de libreria Math <---------------------------#

# Hallar el area y perimetro de un circulo
radio = 5
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}") 

#----------------------------> Uso de libreria Random <---------------------------#
# Simular el lanzamiento de un dado
dado = random.randint(1, 6)
print(f"Lanzamiento de dado: {dado}")

# Seleccionar un elemento aleatorio de una lista
colores = ['rojo', 'azul', 'verde', 'amarillo']
color_aleatorio = random.choice(colores)
print(f"Color aleatorio seleccionado: {color_aleatorio}")

# Barajar cartas
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cartas)
print(f"Cartas barajadas: {cartas}")

#---------------------------> Uso de libreria Statistics <---------------------------#
monthly_sales = {}
with open('Archivos - Test 24\monthly_sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = float(row['sales'])
        monthly_sales[month] = sales

sales_values = list(monthly_sales.values())
mean_sales = statistics.mean(sales_values)
print(f"Promedio de ventas mensuales: {mean_sales}")

sales_values = list(monthly_sales.values())
median_sales = statistics.median(sales_values)
print(f"Mediana de ventas mensuales: {median_sales}")

sales_values = list(monthly_sales.values())
mode = statistics.mode(sales_values)
print(f"Moda de ventas mensuales: {mode}")