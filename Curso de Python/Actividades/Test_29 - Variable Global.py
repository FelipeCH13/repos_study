variable_global = "I am global"

def modify_global():
    global variable_global
    variable_global = "I have been modified globally"

modify_global()
print(variable_global)