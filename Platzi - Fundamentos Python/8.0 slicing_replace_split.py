frase_florentino_perez = "Mbappe es el mejor jugador del mundo"

# Slicing: Obtener una parte de la cadena de texto
print(frase_florentino_perez[0:6])  # Imprime "Mbappe"
print(frase_florentino_perez[7:9])  # Imprime "es"
print(frase_florentino_perez[10:12])  # Imprime "el"
print(frase_florentino_perez[-9:-5]) # Slicing con índices negativos

# Reemplazar una parte de la cadena de texto
nueva_frase = frase_florentino_perez.replace("Mbappe", "Benzema") # Reemplaza "Mbappe" por "Benzema" en la frase original
print(nueva_frase)  # Imprime "Benzema es el mejor jugador del mundo"

frase_segmentada = frase_florentino_perez.split()  # Divide la frase en una lista de palabras
print(frase_segmentada)  

#Normalizacion
print("Mbappe".lower() in frase_florentino_perez.lower())  # Imprime la frase en minúsculas