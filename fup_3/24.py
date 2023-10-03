""" 
O Triângulo de Pascal é um triângulo numérico infinito formado por números
binomiais Cn,k, onde n representa o número da linha (posição horizontal) e k 
representa o número da coluna (posição vertical), iniciando a contagem a partir 
do zero. O triângulo foi descoberto pelo matemático chinês Yang Hui e, 500 anos
depois, várias de suas propriedades foram estudadas pelo francês Blaise Pascal. 
Escreva um programa que leia um número inteiro n ≥ 0 representando a quantidade 
de linhas e em seguida mostre o Triângulo de Pascal com as n linhas.
Exemplo n = 7.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
"""

entrada = int(input())


for i in range(1, entrada+1):
    cont = 1
    for j in range(1, i+1):
        print(cont, end=" ")
        cont = cont * (i-j) // j
    print()

