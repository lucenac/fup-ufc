matriz = []
for linha in range(10):
    l = []
    matriz.append(l)
    for coluna in range(10):
        if linha  < coluna:
            l.append( 2 * linha + 7 * coluna - 2)
        elif linha  == coluna:
            l.append( 3 * linha**2 - 1)
        else:
            l.append(4 * linha**3 - 5 * coluna**2 + 1)

for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f"{matriz[l][c]}\t", end = "")
    print()

