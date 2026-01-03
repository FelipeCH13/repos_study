variable_global = "I am global"

def outer_function():
    variable_global = "I am outer"
    def inner_function():
        variable_global = "I am inner"
        print(variable_global)  # This will print the inner variable

    inner_function()
    print(variable_global)  # This will print the outer variable

outer_function()
print(variable_global)  # This will print the global variable