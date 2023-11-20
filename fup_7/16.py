'''
Faça uma função que receba um vetor e retorne um outro vetor, contendo apenas os
elementos que não aparecem repetidos.
'''

import random
random.seed(0)

def nao_rep(vetor):
    for i in vetor:
        cont = 0
        for j in vetor:
            if i == j:
                cont+=1
            if cont == 2:
                cont = 0
                vetor.remove(i)
                vetor.remove(i)
    vetor.pop(len(vetor)-1)
    return vetor




vetor = []
for i in range(10):
    vetor.append(int(random.uniform(0, 10)))
    
print(nao_rep(vetor))


