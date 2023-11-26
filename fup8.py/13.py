def apresentar_matriz (x):
    for l in range(len(x)):
        for c in range(len(x)):
            print(f"{x[l][c]}\t", end = "")
        print()

def matriz_transposta (y):
    m = []
    for co in range(len(y)):
        c =[]
        m.append(c)
        for lin in range(len(y)):
            c.append(y[lin][co])
    return m

def somatorio(z):
    for linha in range(len(z[0])):
        soma = 0
        for coluna in range(len(z)):
            soma += z[linha][coluna]
        print(soma, end =", ")

pergunta = "S"
while pergunta == "S":
    matriz = []
    for linha in range(5):
        lin = []
        matriz.append(lin)
        for coluna in range(5):
            lin.append(int(input(f"Digite um valor para linha {linha+1}, coluna {coluna+1} para preencher a matriz: ")))
    
    print("/" * 35)
    print("Matriz digita pelo usuário:")
    apresentar_matriz(matriz)

    print("/" * 35)
    print("Matriz transposta:")
    apresentar_matriz(matriz_transposta(matriz))

    print("/" * 35)
    print("A soma de cada linha da matriz transposta:")
    print(somatorio(matriz_transposta(matriz)))
    
    pergunta = input("Gostaria de continuar? [S/N]  ").upper()
print("Finalizando programa...")
