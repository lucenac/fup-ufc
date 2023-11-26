def apresentar_matriz(x):
    for linha in range(len(x)):
        for coluna in range(len(x)):
            print(f"{x[linha][coluna]}\t", end = "")
        print()
# falta arruma como crls irá achar os maiores valores e organizar a saída dos dados. isso acima         

def encontrar_Maior (m):
        maiores = []
        for linha in range(len(m)):
            maiores.append(max(m[linha]))

        for linha in range(len(m)):
            for coluna in range(len(m)):
                maiores.append(max(m[linha]))     
        return (maiores)

pergunta = "S"
while pergunta =="S":
    matriz = []
    matriz_1 = []
    
    for linha in range(3):
        l =[]
        matriz.append(l)
        for coluna in range(3):
            l.append(int(input(f"Digite um número para a matriz 1, linha {linha+1}, coluna {coluna+1}:\n")))

    for linha1 in range(3):
        l1 = []
        matriz_1.append(l1)
        for coluna1 in range(3):
            l1.append(int(input(f"Digite um número para a matriz 2, linha {linha1+1}, coluna {coluna1+1}:\n")))
    
    matriz_os_maiores = encontrar_Maior(matriz) 
    
    print("-*"*20, end = "")
    print("\nA matriz 1: ")
    apresentar_matriz(matriz)
    
    print("-*"*20, end = "")
    print("\nA matriz 2:")
    apresentar_matriz(matriz)
    
    print("-*"*20, end = "")
    print("\nA matriz dos maiores números: ")
    print(matriz_os_maiores)

    pergunta = input("Gostaria de continuar? [S/N]\n").upper()
print("Finalizando o programa...")



    