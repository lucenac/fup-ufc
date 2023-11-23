# Faça uma função que receba dois vetores. Retorne um vetor que seja a intersecção entre os 2
# vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores.
# Esse vetor de retorno não deve conter números repetidos.
def intersecao(v1, v2):
    return list(set(v1) & set(v2))

v1 = list(map(int, input("Vetor 1: ").split()))
v2 = list(map(int, input("Vetor 2: ").split()))

print("Interseção:", intersecao(v1, v2))