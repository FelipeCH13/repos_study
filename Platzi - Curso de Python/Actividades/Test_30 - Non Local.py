def outer_function():
    variable_nonlocal = "I am non-local"

    def inner_function():
        nonlocal variable_nonlocal
        variable_nonlocal = "I have been modified non-locally"
        print(variable_nonlocal)
    inner_function()
    print(variable_nonlocal)
outer_function()

