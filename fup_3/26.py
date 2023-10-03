""" 
Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor 
inteiro positivo n . Calcule o valor do seno desse ângulo usando a respectiva 
série de Taylor: sin(x) = x – x3 /3! + x5 /5! - ... + (-1)n (x**2n+1)/(2n+1)!.
"""


def fat(x):
    num = 1
    for i in range(x , 0, -1):
        num *= i
    return num


def funcao(x, n):
    seno = 0
    for i in range(n):
        form = ((-1) ** i) * (x ** (2 * i + 1)) / fat(2 * i + 1)
        seno += form
    return seno


x1 = float(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y:.8f}")