#Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.

numero=int(input("Digite um número inteiro: "))
divisível3=numero%3==0
divisível5=numero%5==0
if (divisível3 or divisível5) and not (divisível3 and divisível5):
    print("O número é divisível por 3 ou por 5, mas não simultaneamente.")
else:
    print("O número não é divisível por 3, ou por 5.")