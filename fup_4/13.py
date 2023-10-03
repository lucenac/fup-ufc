from math import *


def raiz_quadarada(a,b,c):
    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = -b + sqrt(delta) / (2*a)
        x2 = -b - sqrt(delta) / (2*a)
        return x1, x2
    
    elif delta == 0:
        x1 = -b / (2*a)
        return x1, None
    else:
        return None, None
    
while True:
    a = float(input())
    b = float(input())
    c = float(input())

    if a == 0:
        print('Não é equação de 2° grau')
        break

    x1, x2 = raiz_quadarada(a,b,c)

    if not x1:
        print('Não existe raízes reais!')
        break

    elif not x2:
        print('As raízes são iguais!')
        break
        
    else:
        print(x1, x2)
        break