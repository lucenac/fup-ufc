#V = 4/3 * pi  * r ** 3
#A = 4 * pi * r ** 2
from math import *


def caulculador(x):
    v = 4/3 * pi  * x ** 3
    a = 4 * pi * x ** 2
    return v, a 


raio = float(input())
area, volume = caulculador(raio)
print(f'{area:.2f} {volume:.2f}')