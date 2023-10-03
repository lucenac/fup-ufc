""" 
Faça um programa que calcule e escreva o valor de S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.
"""
s = 0


for i in range(1, 101, 2):
    n = i // 2
    numeros = i / (n+1)
    s += numeros
print(f'{s:.2f}')