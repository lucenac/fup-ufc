""" 
Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura. 
Por exemplo, a saída para n = 4 seria:
*
**
***
****
***
**
*
"""
def tri(x):
    for i in range(1, x+1):
        print('*'*i)
    for i in range(x-1,0,-1):
        print("*"*i)
        
entrada = int(input())

tri(entrada)