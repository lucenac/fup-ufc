""" 
Faça um programa que receba dois números. Calcule e mostre:
◦ A soma dos números pares desse intervalo de números (intervalo incluindo os números
dados);
◦ A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números
dados)
"""
ent1 = int(input())
ent2 = int(input())

soma = 0
mult = 1

if ent1 % 2 == 0:
    for i in range(ent1, ent2+1, 2):
        soma+=i

    for j in range(ent1-1,ent2+2,2):
        mult *= j

if ent1 % 2 != 0:
    for i in range(ent1+1, ent2+2, 2):
        soma+=i

    for j in range(ent1,ent2+1, 2):
        mult *= j

print(soma, mult)
