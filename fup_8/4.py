def encontrar_Maior_menor (m):
        maiores = []
        menores = []
        for linha in range(len(m)):
            maiores.append(max(m[linha]))
            menores.append(min(m[linha]))
                  
        return max(maiores), min(menores)

pergunta = "S"
while pergunta == "S":
    matriz = []
    for linha in range(4):
        l = []
        matriz.append(l)
        for coluna in range(4):
            l.append(int(input(f"Digite um valor para linha {linha+1}, coluna {coluna+1} para preencher a matriz: ")))

    print("A matriz gerada foi: ")
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            print(f"{matriz[l][c]}\t", end = "")
        print()
    print("/"*60)
    print(f"O maior e o menor valor da matriz são respectivamente: {encontrar_Maior_menor(matriz)}")

    pergunta = input("Gostaria de continuar? [S/N]\n").upper()   
print("Fim do programa...")

        