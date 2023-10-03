#Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o resultado obtido.

def soma(x):
    num = 0
    for i in range(1, x + 1):
        num += i
    return num


entrada = int(input(''))
print(soma(entrada))
