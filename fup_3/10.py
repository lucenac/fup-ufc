# Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule xn e retorne o resultado.

def potencia(x, n):
    num = 1
    for i in range(0, n):
        num *= x
    return num

entrada = int(input())
expoente = int(input())

print(potencia(entrada, expoente))