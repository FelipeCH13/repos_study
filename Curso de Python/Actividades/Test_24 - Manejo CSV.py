## Importar librerias
import csv

## Abrir archivo CSV
with open('Archivos - Test 24\products.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    ## Leer y mostrar cada fila del archivo CSV
    for fila in lector_csv:
        print(fila)

## Abrir archivo CSV
with open('Archivos - Test 24\products.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    ## Leer y mostrar cada fila del archivo CSV
    print("\nProductos en el inventario:\n")
    for fila in lector_csv:
        print(f"Producto: {fila[0]}, Precio: {fila[1]}, Cantidad: {fila[2]}")

nuevo_producto = {
    'Producto': 'Auriculares Inalámbricos',
    'Precio': '59.99',
    'Cantidad': '25',
    'Marca': 'SoundWave',
    'Categoria': 'Electrónica'
}

## Escritura en archivo CSV
with open('Archivos - Test 24\products.csv', mode='a', newline='') as archivo_csv:
    archivo_csv.write("\n")
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames  = nuevo_producto.keys())
    ## Escribir filas en el archivo CSV
    escritor_csv.writerow(nuevo_producto)
