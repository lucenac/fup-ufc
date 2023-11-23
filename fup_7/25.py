# Faça uma função que receba dois vetores. Retorne um vetor que seja a união entre os 2
# vetores anteriores, ou seja, que contém os números que estão em qualquer um dos vetores.
# Esse vetor de retorno não deve conter números repetidos.
def uniao(v1, v2):
    return list(set(v1) | set(v2))

v1 = list(map(int, input("Valores 1 separados por espaço: ").split()))
v2 = list(map(int, input("Valores 2 separados por espaço: ").split()))

resultado = uniao(v1, v2)
print("União:", resultado)