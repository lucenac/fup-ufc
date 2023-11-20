import random


vetor = []
pares = []
cont = 0

random.seed(0)
for i in range(15):
    vetor.append(int(random.uniform(0,10)))

for i in vetor:
    if i % 2 == 0:
        pares.append(i)
        cont += 1
        print(i)
print(f'Apareceu {cont} vezes...')
