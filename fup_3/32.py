""" 
Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da
palavra. Imprima a string resultante.
"""
x = input()

ascii = ""

for i in x:
    ascii+=chr(ord(i)+1)
    
print(ascii)