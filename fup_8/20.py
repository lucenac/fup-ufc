def multiplicar_adjacentes(matriz):
    for i in range(20):
        for j in range(20):
            if i > 16 or j > 16: 
                continue

            produto = matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2] * matriz[i+3][j+3]
            if produto > 0:
                return produto, i, j, #direita cima

            produto = matriz[i][j] * matriz[i+1][j-1] * matriz[i+2][j-2] * matriz[i+3][j-3]
            if produto > 0:
                return produto, i, j, #esquerda cima

            produto = matriz[i][j] * matriz[i-1][j+1] * matriz[i-2][j+2] * matriz[i-3][j+3]
            if produto > 0:
                return produto, i, j, #direita baixo

            produto = matriz[i][j] * matriz[i-1][j-1] * matriz[i-2][j-2] * matriz[i-3][j-3]
            if produto > 0:
                return produto, i, j, #esquerda baixo

            produto = matriz[i][j] * matriz[i][j+1] * matriz[i][j+2] * matriz[i][j+3]
            if produto > 0:
                return produto, i, j, #direita

            produto = matriz[i][j] * matriz[i][j-1] * matriz[i][j-2] * matriz[i][j-3]
            if produto > 0:
                return produto, i, j, #esquerda

            produto = matriz[i][j] * matriz[i+1][j] * matriz[i+2][j] * matriz[i+3][j]
            if produto > 0:
                return produto, i, j, #baixo

            produto = matriz[i][j] * matriz[i-1][j] * matriz[i-2][j] * matriz[i-3][j]
            if produto > 0:
                return produto, i, j, #cima

    return "Não há quatro números adjacentes positivos na matriz"

pergunta = "S"

while pergunta == "S":
    matriz = []
    for linha in range(20):
        li = []
        for coluna in range(20):
            li.append(int(input(f"Digite o valor para a linha {linha+1}, coluna {coluna+1}:")))
        matriz.append(li)

    resultado = multiplicar_adjacentes(matriz)

    if isinstance(resultado, tuple):
        print(f"O maior produto de quatro números adjacentes é {resultado[0]}, na posição ({resultado[1] + 1},{resultado[2] + 1}) e na direção {resultado[3]}")
    else:
        print(resultado)
    
    pergunta = input("Gostaria de continuar? [S/N] ").upper()
print("Finalizando progama...")

