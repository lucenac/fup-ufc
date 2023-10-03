entrada = int(input())
cont = 0
for i in range(1,  entrada+1):
    if entrada % i == 0:
        cont+=1
if cont == 2:
    print('O número é primo...')
else:
    print('O número não é primo...')