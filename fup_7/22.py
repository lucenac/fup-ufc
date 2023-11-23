# Faça um programa que preencha um vetor de tamanho 100, com os 100 primeiros naturais
# que não são múltiplos de 7 e não terminam em 7.
v = [i for i in range(1, 1001) if i % 7 != 0 and i % 10 != 7]
print("Vetor:", v)