""" 
◦ 1: Média entre os números digitados
◦ 2: Diferença do maior pelo menor
◦ 3: Produto entre os números digitados
◦ 4: Divisão do primeiro pelo segundo
"""
num1 = float(input())
num2 = float(input())
escolha = int(input())


if escolha == 1:
    saida = (num1 + num2) / 2
    
    
elif escolha == 2:
    if num1 > num2:
        saida = num1 - num2
    elif num2 > num1:
        saida = num2 - num1
    else:
        saida = 0
      
        
elif escolha == 3:
    saida = num1 * num2


elif escolha == 4:
    saida = num1 / num2

else:
    saida = 'Erro, Fim da execução...'
    
print(saida)