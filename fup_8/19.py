import random

def apresentar_matriz (x):
    for l in range(len(x)):
        for c in range(len(x)):
            print(f"{x[l][c]}\t", end = "")
        print()

def media_da_linha_par(lista):
    media_linhas_pares = 0
    qtd_linhas_pares = 0
    for linha in lista:
        for i in range(n_linha):
            if i % 2 == 0:
                soma = sum(linha)
                media = soma / len(linha)
                media_linhas_pares += media
                qtd_linhas_pares += 1
    media = round((media_linhas_pares / qtd_linhas_pares),2)
    return media

def negativos_e_dividi_por3(lista):
    qtd_negativos_e_divisiveis_por_3 = 0
    for i in range(n_linha):
        if i % 2 != 0:
            for elemento in lista[i]:
                if elemento < 0 and elemento % 3 == 0:
                    qtd_negativos_e_divisiveis_por_3 += 1
    return qtd_negativos_e_divisiveis_por_3

pergunta = "S"
while pergunta == "S":
    n_linha  = int(input("Digite a qntd de linhas: "))
    n_coluna  = int(input("Digite a qntd de colunas: "))
    semente = int(input("Digite a semente: "))
    intervalo_min = int(input("Digite o intervalo minimo para gerar: "))
    intervalo_max = int(input("Digite o intervalo máximo para gerar: "))

    random.seed(semente)
    matriz = []
    for linha in range(n_linha):
        li = []
        for coluna in range(n_coluna):
            li.append(random.randint(intervalo_min, intervalo_max))
        matriz.append(li)

    valores = media_da_linha_par(matriz)
    negativo = negativos_e_dividi_por3(matriz)
    
    print("/" *30)
    print("A matriz gerada foi:")
    print(apresentar_matriz(matriz))

    print("/" *30)
    print(f"A média de todos os elementos das linhas pares: {valores}")
    print(f"A qntd de números negativos e que são divisiveis por 3 nas linhas ímpares: {negativo}")

    pergunta = input("Gostaria de continuar? [S/N] ").upper()
print("Finalizando progama...")