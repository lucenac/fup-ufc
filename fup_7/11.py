'''Faça um programa para ler a nota de 15 alunos e armazene em um vetor, calcule e imprima a
média geral.'''
import random
random.seed(0)

notas = []
media = 0

for i in range(15):
    notas.append(random.uniform(0,10))
    
for i in notas:
    media += i
media /= 15

print(f'Média: {media:.2f}')