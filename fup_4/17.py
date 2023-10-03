from math import *


while True:
    entrada = int(input())
    if entrada < 0:
        break
    print(f"O quadrado de {entrada} é {entrada ** 2}, o cubo é {entrada ** 3} e a raíz quadrada é {sqrt(entrada):.2f}")
    
    
print('Fim da execução')