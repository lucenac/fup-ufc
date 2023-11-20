import random

vetor = []
impares = []
soma = 0

random.seed(0)
for i in range(15):
    vetor.append(int(random.uniform(0,10)))

for i in vetor:
    if i % 2 != 0:
        impares.append(i)
        soma += i
        print(i)
print(f'Soma: {soma}')
