#Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

soma = 0
for numero in range(1,1000):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero
print(f"A soma de todos os multiplos de 3 ou 5 abaixo de 1000 é: {soma}")