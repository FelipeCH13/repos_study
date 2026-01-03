## Variable local

variable_global = "I am global"

def local_function():
    local_variable = "I am local"
    print(local_variable)

def show_global():
    print(variable_global)

local_function()
show_global()

## Es posible acceder a la variable global desde cualquier parte del código
print(variable_global)
## No se puede acceder a la variable local fuera de la función
print(local_variable)


