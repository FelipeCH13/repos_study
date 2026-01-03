## Uso de condicionales
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

## Uso de elif
nota = 85
if nota >= 90:
    print("Aprobado con distinción")
elif nota >= 75:
    print("Aprobado")
else:
    print("Reprobado")


## Uso de condicionales con más de una variable
usuario = "admin"
contrasena = "1234"
if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")

## Uso de condicionales con or
dia = "Lunes"
if dia == "Sábado" or dia == "Domingo":
    print("Es fin de semana")
else:
    print("Es día laboral")