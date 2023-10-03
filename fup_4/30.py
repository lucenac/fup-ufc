"""
Escreva um algoritmo que leia certa quantidade de números inteiros e imprima o maior
deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos
deve ser fornecida pelo usuário.
"""

maior = float('-inf') 
menor = float('inf')

for i in range(0, 10):
    entrada = int(input())
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada
print(f"O maior número é {maior} e o menor número é {menor}...")
