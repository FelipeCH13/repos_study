# open(nombre,modo)

# R (read) Lectura
# W (write) Escritura
# X (Crea archivo nuevo)

try:
    f = open("archivo.txt", "r", encoding = "utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("No existe un archivo con el nombre indicado.")


# Uso del With par abrir y cerrar el archivo automaticamente

try:
    with open("archivo.txt","r", encoding = "utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No existe un archivo con el nombre indicado.")
 
# Escritura y lectura de un archivo   
try:
    with open("archivo.txt","w", encoding = "utf-8") as f:
        f.write("Hola mundo vengo directamente desde el Write")
    with open("archivo.txt","r", encoding = "utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No existe un archivo con el nombre indicado.")
    
# Adicion de nuevo contenido con el uso del modo Append
try:
    with open("archivo.txt","a", encoding = "utf-8") as f:
        f.write("\n")
        f.write("Soy una nueva lineaa")
    with open("archivo.txt","r", encoding = "utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No existe un archivo con el nombre indicado.")


# Uso del try/except para la creacion de nuevos archivos
try:
    f = open("archivo_extra.txt", "r", encoding = "utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    open("archivo_extra.txt", "x")
    print("El archivo fue creado.")

