## Validando el tipo de variable
aprendiendo = "Voy en las primeras clases"
print(type(aprendiendo))

## Formas de difinir variables Strings
prueba_1 = "Hola"
prueba_2 = 'Hola Hola Holaaa'
## Posibilidad de agregar salto de linea
prueba_3 = '''Holaaaaaa 


soy otra prueba   '''
print(prueba_3)


## Uso de indexacion, identificacion de valores en una posicion
aprendiendo = "Sigo en las primeras clases"
## De derecha a izquierda
print(aprendiendo[0])
## De izquierda a derecha, utilizar negativos
print(aprendiendo[-2])

## Concatenacion de strings
print(prueba_1 +" "+ aprendiendo)

## Replicar los strings
print(prueba_2 * 5)

##Consultar la longiud de los caracteres, el espacio cuenta como caracter
print(len(aprendiendo))

##Uso de metodos de las variables
print(aprendiendo.upper())
print(aprendiendo.lower())
print(prueba_3.strip())

## Concatenar con espacios
print("Nunca", "pares", "de", "aprender")

## Uso de separadores
print("Nunca", "pares", "de", "aprender", sep=", ")


## Uso de end como salto
print("Nunca", end=" ")
print("pares de aprender")

# Uso de f-strings para ingresar variables en la impresion
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")

#     Formato
#       Es otra forma de insertar valores similares a f-string
frase = "nunca pares de aprender"
autor = "platzi"
print("frase: {}, autor: {}\n".format(frase,autor))

#     Formatos especificos 
#       Controlasmos el formato en que se va a imprimir los numeros 

valor = 3.14159
print("Valor: {:.2f}".format(valor))

#     Salto de linea y caracteres especiales 
#           los saltos de linea se indican con un \n al final de la cadena 
print("Hola\nmundo")

#           Para imprimir unas commilas dobles o simples ocupamos diagonales (\) antes de las comillas
print('Hola soy \'Pipe\'\n')

#           Para imprimir una diagonal ocupamos dobles diagonales (\\)