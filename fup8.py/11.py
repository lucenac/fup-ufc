pergunta = "S"
while pergunta == "S":
    matriz = []
    for linha in range(4):
        l = []
        matriz.append(l)
        for coluna in range(4):
            l.append(int(input(f"Digite um valor para linha {linha+1}, coluna {coluna+1} para preencher a matriz: ")))
        
    print("/" * 35)
    print("Matriz digita pelo usuário:")
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            print(f"{matriz[l][c]}\t", end = "")
        print()
    
    print("/" * 35)
    soma = matriz[0][3] + matriz[1][2] + matriz[2][1] + matriz[3][0]
    print(f"A soma da diagonal secundária da matriz é {soma}")

    pergunta = input("Gostaria de continuar? [S/N]  ").upper()
print("Finalizando programa...")
