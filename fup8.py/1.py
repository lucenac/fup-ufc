import random
random.seed(0)

def criar_matriz(entrada1=1, entrada2=1, tipo='str'):    
    v = []
    for i in range(entrada1):
        v.append([])
    
    if tipo == 'int':
        for i in range(0,entrada1):
            for j in range(0,entrada2):
                v[i].append(int(f'{random.uniform(0,99):.0f}'))
    
    else:
        for i in range(0,entrada1):
            for j in range(0,entrada2):
                v[i].append(f'{random.uniform(0,99):.0f}')
        
    return v


v = criar_matriz(4,4,'int')



cont = 0

for i in range(len(v)):
    for j in v[i]:
        if j >= 10:
            cont+=1
print(f'Quantidade de item(ns) maior(es) que 10: {cont}')