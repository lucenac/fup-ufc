#print('='*int(input()))

""" 
Faça um programa que desenhe uma linha na tela usando vários símbolos de igual (Ex:
========). O programa deve ler quantos sinais de iguais serão mostrados.
"""

entrada = int(input())

for i in range(0, entrada):
    print("=", end='')