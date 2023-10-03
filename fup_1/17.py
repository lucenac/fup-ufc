# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

iv1 = float(input())
iv2 = float(input())
iv3 = float(input())

vp = float(input())

ivt = iv1 + iv2 + iv3

ivf1 = (iv1 / ivt) * vp
ivf2 = (iv2 / ivt) * vp
ivf3 = (iv3 / ivt) * vp

print(f'{ivf1:.2f}')
print(f'{ivf2:.2f}')
print(f'{ivf3:.2f}')
