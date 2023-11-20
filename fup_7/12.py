'''Faça uma uma função que receba um vetor com as notas de vários alunos e retorne tanto a
média geral quanto o desvio padrão (populacional).'''

import random
import math


def media_dp(notas,qnt_alu):
    media = 0
    dp = 0
        
    for i in notas:
        media += i    
    media /= qnt_alu

    for i in notas:
        dp += (i-media) ** 2
    dp = math.sqrt(dp / qnt_alu)
    
    return f'Média: {media:.2f} | Desvio Padrão: {dp:.2f}'

    
random.seed(0)
        
notas = []
qnt_alu = 15

for i in range(qnt_alu):
    notas.append(random.uniform(0,10))
    
print(media_dp(notas,qnt_alu))