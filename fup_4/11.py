num1 = float(input())
escolha = int(input())
num2 = float(input())

if escolha == 1:
    saida = num1 + num2
elif escolha == 2:
    saida = num1 - num2
elif escolha == 3:
    saida = num1 * num2
elif escolha == 4:
    saida = num1 / num2
else:
    saida = ('Opcao invalida')
    
print(saida)