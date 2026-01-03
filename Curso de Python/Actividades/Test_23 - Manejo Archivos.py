## Apertura de los archivos
with open("Archivos - Test 23\cuento.txt", "r") as archivo_texto:
    for lineas in archivo_texto:
        print(lineas.strip())

## Probando sin strip()
with open("Archivos - Test 23\cuento.txt", "r") as archivo_texto:
    for lineas in archivo_texto:
        print(lineas)

## Uso de read line()
with open("Archivos - Test 23\cuento.txt", "r") as archivo_texto:
    lineas = archivo_texto.readlines()
    print(lineas)

## Escritura en archivos
with open("Archivos - Test 23\cuento.txt", "w") as archivo_escritura:
    archivo_escritura.write("Esta es una línea escrita en el archivo.\n")
    archivo_escritura.write("Esta es otra línea escrita en el archivo.\n")
    archivo_escritura.write("Fin del archivo de escritura.\n")
    
## Verificación de la escritura
with open("Archivos - Test 23\cuento.txt", "r") as archivo_verificacion:
    for lineas in archivo_verificacion:
        print(lineas.strip())
