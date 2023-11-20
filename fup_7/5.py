conjunto1 = []
conjunto2 = []

for i in range(10):
    entrada = float(input('Insira um valor: '))
    conjunto1.append(entrada)

for numero in conjunto1:
    conjunto2.append(numero ** 2)
    print(numero)

for numero in conjunto2:
    print(numero)
