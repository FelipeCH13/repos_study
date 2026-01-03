### Juego Piedra Papel y Tijera
print("Bienvenido al Juego Piedra, Papel y Tijera")
## Solicitud de información
print("A continuación por favor ingresa el nombre del jugador 1:")
jugador1 = input()
print("A continuación por favor ingresa el nombre del jugador 2:")
jugador2 = input()
## Impresión de los nombres de los jugadores
print("Muy bien", jugador1, "y", jugador2, "comencemos el juego")
# Diccionario de opciones
opciones_map = {1: "Piedra", 2: "Papel", 3: "Tijera"}
print("Por favor elige una opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
# Solicitar elecciones de los jugadores
eleccion1 = int(input(jugador1 + ", ingresa el número de tu elección:"))
eleccion2 = int(input(jugador2 + ", ingresa el número de tu elección:"))
# Validar elecciones y determinar el ganador
if eleccion1 < 1 or eleccion1 > 3 or eleccion2 < 1 or eleccion2 > 3:
    print("Elección inválida. Por favor elige un número entre 1 y 3.")
else:
    # Mostrar elecciones
    eleccion1_nombre = opciones_map.get(eleccion1, "Elección inválida")
    eleccion2_nombre = opciones_map.get(eleccion2, "Elección inválida")
    print(jugador1, "eligió:", eleccion1_nombre)
    print(jugador2, "eligió:", eleccion2_nombre)
    # Determinar el ganador
    if eleccion1 == eleccion2:
        print("Es un empate!")
    elif (eleccion1 == 1 and eleccion2 == 3) or (eleccion1 == 2 and eleccion2 == 1) or (eleccion1 == 3 and eleccion2 == 2):
        print(jugador1, "gana!")
    else:
        print(jugador2, "gana!")