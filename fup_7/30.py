# Dado um vetor de n elementos, descubra se existem segmentos iguais máximos.
def maximo(vetor):
    n = len(vetor)
    iniciomax = -1
    tammax = -1

    for i in range(n - 1):
        for j in range(i + 1, n):
            k = 0
            while j + k < n and vetor[i + k] == vetor[j + k]:
                k += 1

            if k >= 2 and k > tammax:
                iniciomax = i
                tammax = k

    if iniciomax == -1 or tammax == -1:
        return -1, -1, -1
    else:
        return iniciomax, tammax, vetor[iniciomax:iniciomax + tammax]

v = list(map(int, input("Valores separados por espaço: ").split()))

result = maximo(v)

if result[0] == -1:
    print("Inválido")
else:
    print(f"Segmento máximo: {result[2]}, inicia na posição {result[0]} e tem tamanho {result[1]}.")