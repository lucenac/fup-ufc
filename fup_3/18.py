""" 
Faça uma função que receba um número inteiro positivo P e retorne a soma dos 
algarismos De P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos 
é 2 + 4 = 6.
"""

def fatorial(x):
    num = 1
    for i in range(x , 0, -1):
        num *= i
    return num

def estranho(n):
    valor1 = fatorial(n) // 10
    valor2 = fatorial(n)  % 10
    return valor1 + valor2

entrada = int(input())
print(estranho(entrada))