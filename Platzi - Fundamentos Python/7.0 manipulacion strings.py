print("Hello, 'World!'")  # Imprime un mensaje con comillas simples dentro de comillas dobles
print('Hello, "World!"')  # Imprime un mensaje con comillas dobles dentro de comillas simples

# Unica forma de incluir saltos de línea en una cadena de texto es usando comillas triples
multiples = """líneas de texto
con saltos de línea
y más texto"""
print(multiples)  # Imprime el texto con saltos de línea

#Conteo de caracteres
texto = "Hola, mundo!"
print(len(texto))  # Imprime la cantidad de caracteres en el texto

#Busqueda de palabras
frase = "Python es un lenguaje de programación"
print(frase.find("lenguaje"))  # Imprime la posición de la palabra "lenguaje" en la frase
print(frase.find("Java"))  # Imprime -1 porque la palabra "Java" no se encuentra en la frase

# Verificación de inclusión
estaIncluida = "programación" in frase  # Verifica si la palabra "programación" está en la frase
print(estaIncluida)  # Imprime True porque la palabra "programación" está en la frase
noEstaIncluida = "Java" not in frase  # Verifica si la palabra "Java" no está en la frase
print(noEstaIncluida)  # Imprime True porque la palabra "Java" no

mayuscula = frase.upper()  # Convierte la frase a mayúsculas
print(mayuscula)  # Imprime la frase en mayúsculas

# El metodo STRPIP elimina los espacios en blanco al principio y al final de una cadena de texto
espacios = "   Hola, mundo!   "
print(espacios.strip())  # Elimina los espacios en blanco al principio y al final