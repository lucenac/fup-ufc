for numero in range(1000, 10000):
    parte1 = numero // 100
    parte2 = numero % 100 
    
    soma = parte1 + parte2
    quadrado = soma ** 2

    if quadrado == numero:
        print(numero)

