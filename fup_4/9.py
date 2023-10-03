num1 = int(input())
num2 = int(input())
num3 = int(input())

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor= num3
    
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

meio = num1 + num2 + num3 - menor - maior

print(menor,meio,maior)

