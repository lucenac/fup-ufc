def gerar_matriz(m):
    matr = []
    for linha in range(4):
        lin = []
        matr.append(lin)
        for coluna in range(5):
            lin.append(int(input(f"Digite um valor para linha {linha+1}, coluna {coluna+1} para preencher: ")))
    return matr

def apresentar_matriz (x):
    for l in range(len(x)):
        for c in range(len(x)):
            print(f"{x[l][c]}\t", end = "")
        print()


def soma_de_matriz(a,b):
    matriz_somada = []
    for linha in range(len(a)):
        matriz_somada.append([])
        for coluna in range(len(a)):
            matriz_somada[linha].append(a[linha][coluna] + b[linha][coluna])
    return matriz_somada

pergunta = "S"
while pergunta == "S":
    matriz1 = ()
    matriz2 = ()
    
    print("Agora irá digitar os números para a matriz 1!")
    matriz1 = gerar_matriz(matriz1)
    print("/" * 30)
    
    print("Agora irá digitar os números para a matriz 2!")
    matriz2 = gerar_matriz(matriz2)
    print("/" * 30)

    print("Matriz 1 ")
    apresentar_matriz(matriz1)
    print("/" * 30)
    print("Matriz 2")
    apresentar_matriz(matriz2)
    
    print("/" * 30)
    print("A soma das matrizes 1 e 2:")
    apresentar_matriz(soma_de_matriz(matriz1,matriz2))
    print("/" * 30)
    
    pergunta = input("Gostaria de continuar? [S/N]  ").upper()
print("Finalizando programa...")
