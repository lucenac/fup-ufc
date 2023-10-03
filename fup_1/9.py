# Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.

from math import *


g = float(input())
r = g * pi / 180
print(f'{r:.2f}')