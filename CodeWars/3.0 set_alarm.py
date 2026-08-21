## Mi version de solucion
def set_alarm(employed, vacation):
    # Your code here
    if employed is True and vacation is False:
        return True
    else:
        return False

#Solucion optimizada
def set_alarm(employed, vacation):
    return employed and not vacation