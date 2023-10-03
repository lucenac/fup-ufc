''' 
O número de Fibonacci Fn para n> 0 é definido da seguinte maneira:
◦ F1 = 1
◦ F2 = 1
◦ Fn = Fn-1 + Fn-2 para n> 2
Faça uma função que receba um valor inteiro n e calcule e Fn.
'''

def fibonacci(f):
    f1 = f2 = 1
    fn = 0
    
    for i in range(3, f + 1):
        fn = f1 + f2
        f2 = f1
        f1 = fn
    return fn

entrada= int(input())
print(fibonacci(entrada))