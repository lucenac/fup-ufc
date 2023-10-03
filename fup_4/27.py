maior = float('-inf') 
menor = float('inf')

saida = 1

while saida == True:
    entrada = int(input())
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada
    opcao = input('deseja continuar? [s/n] ')
    if opcao == 'n':
        saida = False
    
print(f"O maior número é {maior} e o menor número é {menor}...")
     