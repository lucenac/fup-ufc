# Faça um vetor de tamanho 70 preenchido com o seguinte valor: (i + 5*i) % (i + 1) , sendo i a
# posição do elemento no vetor. Em seguida imprima o vetor na tela.
vetor = [(i + 5 * i) % (i + 1) for i in range(0, 70)]
print("Vetor:", vetor)