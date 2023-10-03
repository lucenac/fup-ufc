# Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.

entrada = int(input())


horas = entrada // 3600
minutos = (entrada % 3600) // 60
segundos = entrada % 60


print(f'{horas}') 
print(f'{minutos}') 
print(f'{segundos}') 
