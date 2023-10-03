# Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).

def soma_par(x):
    num = 0
    for i in range(0, x + 1, 2):
        num += i
    return num


entrada = int(input(''))
print(soma_par(entrada))
