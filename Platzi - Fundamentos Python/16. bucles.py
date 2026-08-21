## Bucle While
# i = 1

# while i <= 10: ## Definicion del iterador
#     print(i)
#     if i == 5:
#         break ##Permite romper el bucle
#     i += 1 ##Se incrementa el iterador, luego de la instruccion
    
# a = 0
# while a < 10: ## Definicion del iterador
#     a += 1 ##Se incrementa el iterador, luego de la instruccion
#     if a == 5:
#         continue ##Permite saltar una instruccion dentro del bucle
#     print(a)

# b = 1
# while b <= 10: ## Definicion del iterador
#     print(b)
#     b += 1 ##Se incrementa el iterador, luego de la instruccion
# else:
#     print("Se completaron las iteraciones necesarias")
    
## Bucle For

palabra = "Wonderwall"

for letra in palabra:
    print(letra)
    
jugadores = ["Bellingham","Kane","Spence"]

for jugador in jugadores:
    if jugador == "Kane":
        break ## Permite romper el ciclo en caso de que se cumpla la condicion
    print(jugador)

for jugador in jugadores:
    if jugador == "Kane":
        continue ##Permite saltar una instruccion dentro del bucle
    print(jugador)
    
    
## Range

for i in range(10): #El numero indicado no es incluido dentro del ciclo
    print("Llegue hasta el: ",i)
    
for i in range(3,5): #Inicia en 3 y termina en 5 sin incluirlo, dando como resultado los valores 3 y 4
    print("El numero seleccionado es: ",i)
    
for i in range(0,10,2): ## El tercer parametro indica el salto entre un valor y otro
    print("El numero seleccionado es: ",i)


resultados = ["Ganadores","Perdedores","No supe que poner"]

for resultado in resultados:
    for jugador in jugadores:
        print(resultado,jugador)
        
for jugador in jugadores:
    for resultado in resultados:
        print(jugador,resultado)