""" 
Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, 
conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! ... 1/n!.
"""

def fatorial(x):
    num = 1
    for i in range(x , 0, -1):
        num *= i
    return num

def fat_harm(n):
    cont = 0
    for i in range(1, n+1):
        cont += 1/fatorial(i)
    return cont


entrada = int(input())
print(fat_harm(entrada))