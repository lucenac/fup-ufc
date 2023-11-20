vetor = []
maior = float('-inf')
menor = float('inf')

for i in range(1,11):
    entrada = int(input(f'Digite o {i}° valor: '))
    vetor.append(entrada)

for i in vetor:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'Maior:{maior} | Menor: {menor}')