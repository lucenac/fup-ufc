""" 
Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
◦ O primeiro ganhador receberá 46%;
◦ O segundo ganhador receberá 32%;
◦ O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

entrada = float(input())

primeiro = entrada * (46/100)
segundo = entrada * (32/100)
terceiro = entrada * (22/100)

print(f'{primeiro:.2f}')
print(f'{segundo:.2f}')
print(f'{terceiro:.2f}')