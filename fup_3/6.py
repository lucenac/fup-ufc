#Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.
entrada = int(input())
cont = 0

for i in range(1, entrada + 1):
    cont += i
    
print(cont)



