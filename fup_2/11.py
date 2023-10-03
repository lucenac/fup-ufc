def quadrado(x=0, y=0, z=0):
    calculo1 = x ** 2 + y ** 2 + z ** 2
    calculo2 = (x + y + z) ** 2
    return calculo1, calculo2

entrada1 = float(input())
entrada2 = float(input())
entrada3 = float(input())

saida1, saida2 = quadrado(entrada1, entrada2, entrada3)

print(saida1, saida2)