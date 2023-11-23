'''
Faça uma função que receba um vetor e retorne um outro vetor, contendo apenas os
elementos que não aparecem repetidos.
'''

def norep(v):
    return [x for x in v if v.count(x) == 1]

vetor = [int(input(f"Digite o valor para a posição {i + 1}: ")) for i in range(0, 10)]
resultado = norep(vetor)

print("Sem repetições:", resultado)