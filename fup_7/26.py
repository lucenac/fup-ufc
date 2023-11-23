# Faça uma função que receba dois vetores. Retorne um vetor que seja a diferença entre os 2
# vetores anteriores, ou seja, que contém os números que estão no primeiro vetor mas não no
# segundo vetor. Esse vetor de retorno não deve conter números repetidos.
def diferenca(v1, v2):
    return list(set(v1) - set(v2))

v1 = list(map(int, input("Valores 1 separados por espaço: ").split()))
v2 = list(map(int, input("Valores 2 separados por espaço: ").split()))

resultado = diferenca(v1, v2)
print("Diferença:", resultado)