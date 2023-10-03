#Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.
v1 = float(input())
v2 = float(input())
v3 = float(input())

sq = v1 ** 2 + v2 ** 2 + v3 ** 2

qs = (v1 + v2 + v3) ** 2

print(f'{sq:.2f}')
print(f'{qs:.2f}')
