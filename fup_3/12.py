#Escreva uma função que receba k e n ≥ k ≥ 0 e calcule o coeficiente binomial Cn,k = n!/(k! *(n-k)!)


def fatorial(x):
    num = 1
    for i in range(x , 0, -1):
        num *= i
    return num


def coef_bin(k, n):
    Cn = fatorial(n)/(fatorial(k) *fatorial(n-k))
    return Cn


num1 = int(input())
num2 = int(input())

print(coef_bin(num1,num2))
