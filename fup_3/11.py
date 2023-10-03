#Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.

def fatorial(x):
    num = 1
    for i in range(x , 0, -1):
        num *= i
    return num

entrada = int(input())
print(fatorial(entrada)) 