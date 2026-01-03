import json
import json

# Leer el archivo JSON
with open('Archivos - Test 25\\products.json', 'r', encoding='utf-8') as file:
    productos = json.load(file)

# Normalizar posibles estructuras: el JSON podría ser una lista de productos
# o un dict que contiene la lista (por ejemplo {"products": [...]})
if isinstance(productos, dict):
    if 'products' in productos and isinstance(productos['products'], list):
        productos = productos['products']
    else:
        for v in productos.values():
            if isinstance(v, list):
                productos = v
                break

# Mostrar cada producto y sus campos (protegiendo accesos)
for producto in productos:
    if isinstance(producto, dict):
        print(f"Name: {producto.get('name', '<sin name>')}, Price: {producto.get('price', '<sin price>')}")
    else:
        print("Elemento inesperado en la lista de productos:", repr(producto))


## Ingresar registros en el archivo JSON
nuevos_productos = [
    {"name": "Mouse Logitech", "price": 100, "quantity": 50, "brand": "Logitech", "category": "Peripherals", "entry_date": "2024-06-01"},
    {"name": "Mousepad Redragon", "price": 200, "quantity": 30, "brand": "Redragon", "category": "Peripherals", "entry_date": "2024-06-02"},
]

# Abrir, cargar, extender correctamente y reescribir
with open('Archivos - Test 25\\products.json', 'r', encoding='utf-8') as file:
    productos_actuales = json.load(file)

# Ajustar estructura antes de extender
if isinstance(productos_actuales, dict):
    if 'products' in productos_actuales and isinstance(productos_actuales['products'], list):
        productos_actuales['products'].extend(nuevos_productos)
        salida = productos_actuales
    else:
        # si hay otra clave con lista, añadir allí
        added = False
        for k, v in productos_actuales.items():
            if isinstance(v, list):
                v.extend(nuevos_productos)
                added = True
                break
        if not added:
            # envolver el contenido anterior en una lista y añadir
            salida = [productos_actuales]
            salida.extend(nuevos_productos)
        else:
            salida = productos_actuales
elif isinstance(productos_actuales, list):
    productos_actuales.extend(nuevos_productos)
    salida = productos_actuales
else:
    salida = [productos_actuales]
    salida.extend(nuevos_productos)

with open('Archivos - Test 25\\products.json', 'w', encoding='utf-8') as file:
    json.dump(salida, file, indent=4, ensure_ascii=False)

print("Actualización completada.")