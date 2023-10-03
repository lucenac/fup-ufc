"""Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas
notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas
notas de 100, 50, 20, 10, 5, 2 e 1 real."""


entrada = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
contagem = {}


for nota in notas:
    quantidade = entrada // nota
    if quantidade > 0:
        contagem[nota] = quantidade
        entrada -= quantidade * nota
    else:
        contagem[nota] = 0

for q in contagem:
    print(contagem[q])
