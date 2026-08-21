# Mi version de solucion
import math

def square_area(a):
    r = (a * 4) / (2 * math.pi) 
    area = r ** 2
    return area

# Version optimizada
def square_area(a):
    return ((2 * a) / math.pi) ** 2