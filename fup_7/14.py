''' 
Faça um programa que preencha um vetor com 12 números reais aleatórios (uniformemente
distribuídos no intervalo [-10, 10]), mostre esses números, e calcule a quantidade de
números negativos e a soma dos números positivos desse vetor. A semente dos números
aleatórios será dada como entrada para o programa.
'''
import random

entrada = int(input('Digite a semente: '))
random.seed(entrada)

vetor = []
cont_neg = 0
soma = 0

for i in range(12):
    vetor.append(random.uniform(-10,10))

for i in vetor:
    if i < 0:
        cont_neg += 1
    elif i >= 0:
        soma += i
        
print(f'Semente: {entrada} | Quantidade de números negativos: {cont_neg} | Soma de positivos: {soma:.2f}')