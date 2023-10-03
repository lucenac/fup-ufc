
while True:
    num1 = float(input("Número 1: "))
    print("""1-Soma
2-Subtração
3-Multiplicação
4-Divisão
5-Sair""")
    escolha = int(input())
    num2 = float(input("Número 2: "))
    
    if escolha == 1:
        saida = num1 + num2
        print(saida)
    elif escolha == 2:
        saida = num1 - num2
        print(saida)
    elif escolha == 3:
        saida = num1 * num2
        print(saida)
    elif escolha == 4:
        saida = num1 / num2
        print(saida)
    elif escolha == 5:
        break
    else:
        print('Opcao invalida')
    
    
