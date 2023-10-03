""" 
Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o 
resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + ... + (n**2 + 1)/(n + 3)
"""

def soma(n):
    cont = 0
    for i in range(1, n+1):
        s = (i**2 + 1) / (i + 3)
        cont += s
    return cont

entrada = int(input())

vari = soma(entrada)
print(f"{vari:.2f}")