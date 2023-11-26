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

def inverter (x):
    return (-(x))

def primo_teste(x):
    contador = 0
    if x == 2:
        print("É primo!")
        return x
    
    for i in range(1, x+1):
        if x % i == 0:
            contador +=1
        else:
            continue
    
    if contador == 2:
        return x
    else:
        False

def analisar_primo(lista):
    primos = []
    for i in lista:
        if i > 0:
            if primo_teste(i) == True:
             primos.append(i)
        elif i < 0:
            x = inverter(i)
            if primo_teste(x) == True:
                primos.append(i)
    if not primos:
        return 0
    else:
        return tuple(primos)
    
def maior_menor(lista):
    if analisar_primo(lista) == 0:
        return min(lista)
    else:
        return max(analisar_primo(lista))

def dividindo(num1, num_divisor):
    return (num1/ num_divisor)

pergunta = "S"
while pergunta == "S":
    matriz = []
    for linha in range(12):
        linha_guarda = []
        matriz.append(linha_guarda)
        for coluna in range(13):
            linha_guarda.append(int(input(f"Digite um valor para a linha {linha +1}, coluna {coluna+1}:  ")))
    
    matriz_trocada = matriz_transposta(matriz)
    matriz_resultado = []
    for l in range(len(matriz_trocada)):
        lis = []
        lis_analise = maior_menor(matriz_trocada[l])
        num = int(lis_analise)
        for c in range(len(matriz_trocada[l])):
            numero = matriz_trocada[l][c]
            resultado = round(dividindo(numero,num), 2)
            lis.append(resultado)
        matriz_resultado.append(lis)
            
    print("=" * 30)
    print("A matriz gerada pelo usuário:")
    apresentar_matriz(matriz)

    print("=" * 30)
    print("O resultado:")
    apresentar_matriz(matriz_transposta(matriz_resultado))

    pergunta = input("Gostaria de continuar? [S/N] ").upper()
print("Finalizando programa...")