""" 
Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . 
Por exemplo, a saída para n = 6 seria:

     *
    ***
   *****
  *******
 *********
***********
"""

def tri(x):
    espacos = 2 * x - 1
    for i in range(1, x*2, 2):
        print(" " * (espacos // 2), end='')
        print('*'*i)
        espacos -= 2


entrada = int(input())
tri(entrada)