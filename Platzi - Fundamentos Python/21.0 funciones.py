## Funciones: Bloques de codigo que solo se ejecutan cuando son llamdos, permiten organizar y modularizar el codigo.
def mi_primera_funcion():
    print("Hola estoy probando mi funcion")
    
mi_primera_funcion()

## Funciones con argumentos
def mi_segunda_funcion(nombre): ## Argumento: Variables que espera una funcion
    print("Hola estoy conciendo a:",nombre)
    
mi_segunda_funcion("Pedrito") ## Parametro: Valores que se pasan a la función
mi_segunda_funcion("Pedritooooo")

#Uso de varios argumentos
## Funciones con argumentos
def mi_segunda_funcion(nombre,edad = 18): ##Uso de valores predeterminados
    print("Hola estoy conciendo a:",nombre, "quien tiene:",edad)
    
mi_segunda_funcion("Pedrito",30) ## Parametro: Valores que se pasan a la función
mi_segunda_funcion("Pedritooooo") ## Valor predeterminado asignado

def sumar(a,b):
    return a + b

resultado = sumar(333,111) ## El resultado de una funcion matematica se debe asignar a una variable
print(resultado)


## FUNCIONES LAMBDA
# SINTAXIS LAMBDA ARGUMENTOS:EXPRESION
x = lambda a: a ** a
print(x(7))

## Uso de 2 argumentos
y = lambda a,b: a ** b
print(y(2,4))

## Fabrica de funciones
def fabrica(n):
    return lambda a: a * n

duplicador = fabrica(2)
triplicador = fabrica(3)

print(duplicador(5)) #10
print(triplicador(5)) #15