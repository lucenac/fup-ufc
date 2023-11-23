# Faça uma função que, dado um vetor de números reais, ordene os elementos
# desse vetor do maior para o menor, e retorne o vetor ordenado.
# Não use nenhuma função de ordenação do python.
def ordem(valores):
    n = len(valores)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if valores[i] < valores[j]:
                valores[i], valores[j] = valores[j], valores[i]
    return valores

v = list(map(float, input("Digite os valores do vetor separados por espaço: ").split()))

vordenado = ordem(v)
print("Vetor ordenado do maior para o menor:", vordenado)