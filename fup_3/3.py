#Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.
soma = 0

for i in range(0, 10):
    num = int(input(""))
    soma += num
print(soma)