# Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.
s = float(input())

aumento = s*(21.37 / 100)

novo_s = s + aumento

print(f'{novo_s:.2f}')