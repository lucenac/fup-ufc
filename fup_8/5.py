def numero_x_na_matriz (m, x):
    
    for linha in range(len(m)):
        for coluna in range(len(m)):
            if m[linha][coluna] == x:
                return (linha+1),(coluna+1)
    else:
        return -1

pergunta = "S"
while pergunta == "S":
    matriz = []
    for linha in range(5):
        l = []
        matriz.append(l)
        for coluna in range(5):
            l.append(int(input(f"Digite um valor para linha {linha+1}, coluna {coluna+1} para preencher a matriz: ")))

    print("A matriz gerada foi: ")
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            print(f"{matriz[l][c]}\t", end = "")
        print()
    
    print(f"/" * 60, end = "")
    N_encontrar = int(input("\nDigite um número que deseja encontrar: "))
    
    resultado = numero_x_na_matriz(matriz, N_encontrar)
    if resultado == -1 :
        print("Não há este valor na matriz")
    else:
        print(f"O valor está na linha {resultado[0]}, coluna {resultado[1]}")

    pergunta = input("Gostaria de continuar? [S/N]\n").upper()   
print("Fim do programa...")

        