''' 
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais, se
sim escreva esses valores na tela.
'''
# [8, 7, 4, 2, 5, 4, 7, 3, 4, 5]
import random
random.seed(0)

vetor = []
comparar = []

for i in range(10):
    vetor.append(int(random.uniform(0, 10)))
print(vetor)

for i in vetor:
    cont = 0
    for j in vetor:
        if i == j:
            cont+=1
        if cont == 2:
            cont = 0
            vetor.remove(i)
            print(f'{i} aparece mais de uma vez...')

print(vetor)
