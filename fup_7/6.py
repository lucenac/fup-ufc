
sequencia = []

for i in range(0,8):
    entrada = int(input('Insira um valor:'))
    sequencia.append(entrada)

x = int(input("Insira um valor de posição: ")) 
y = int(input("Insira um valor de posição: ")) 

soma = sequencia[x] + sequencia[y]

print(f'A sequência de {sequencia[x]} + {sequencia[y]} é igual a {soma}')