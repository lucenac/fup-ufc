'''Leia um vetor de 20 inteiros e atribua 0 para todos os elementos que possuírem valores
negativos.'''
import random


vetor = []
random.seed(0)

for i in range(20):
    vetor.append(int(random.uniform(-99,99)))

for i in range(len(vetor)):
    if vetor[i] < 0:
        vetor[i] = 0
    print(vetor[i])