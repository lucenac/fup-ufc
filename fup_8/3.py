
entrada1=int(input('Número de colunas: '))
entrada2= int(input('Número de linhas: '))
v = []

for i in range(entrada1):
    v.append([])
    

for i in range(0,entrada1):
    for j in range(0,entrada2):
        v[i].append(f'|{i} {j}| ')
        
        
for coluna in range(len(v)):
    for linha in range(len(v[coluna])):
        print(v[coluna][linha],end=' ')
    print()