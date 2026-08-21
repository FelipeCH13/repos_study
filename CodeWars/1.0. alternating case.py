def to_alternating_case(string):
    resultado = ""
    for index, char in enumerate(string):
        if char.isupper():
            if char.isalpha():
                resultado += char.lower()
            else:
                resultado += char
        else:
            if char.isalpha():
                resultado += char.upper()
            else:
                resultado += char
    return resultado