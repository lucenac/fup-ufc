''' 
Faça uma função que receba um vetor com as notas de vários alunos, e retorne a média
geral, o desvio padrão (populacional), e quantos alunos estão com nota menor que 7.0.
'''
import random
import math


def media_dp(notas,qnt_alu):
    media = 0
    dp = 0
    nota_baixa = 0
        
    for i in notas:
        media += i    
    media /= qnt_alu

    for i in notas:
        dp += (i-media) ** 2
    dp = math.sqrt(dp / qnt_alu)
    
    for i in notas:
        if i < 7:
            nota_baixa += 1
    
    return f'Média: {media:.2f} | Desvio Padrão: {dp:.2f} | Número de notas baixas: {nota_baixa}'

    
random.seed(0)
        
notas = []
qnt_alu = 15

for i in range(qnt_alu):
    notas.append(random.uniform(0,10))
    
print(media_dp(notas,qnt_alu))