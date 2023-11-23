# Faça uma função que receba um vetor posições e o compacte, ou seja, elimine as posições
# com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos
# uma posição para trás no vetor. No final, retorne o vetor compacto.
def compactar(vetor):
    return [num for num in vetor if num != 0]

voriginal = [1, 0, 2, 0, 0, 3, 4, 0, 5, 0]
vcompactado = compactar(voriginal)
print("Compactado:", vcompactado)