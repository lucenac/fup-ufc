#Faça uma função que receba 2 números inteiros positivos e calcule o Máximo Divisor Comum (MDC).

def calcular_mdc(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > 0 and n2 > 0:
    mdc = calcular_mdc(n1, n2)
    print(f"O MDC de {n1} e {n2} é {mdc}.")
else:
    print("Ambos os números devem ser inteiros positivos.")