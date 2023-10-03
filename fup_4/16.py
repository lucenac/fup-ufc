maior = float('-inf')
menor = float('inf')

while True:
    entrada = float(input())
    if entrada < 0:
        break
    
    if entrada > maior:
        maior = entrada
        
    if entrada < menor:
        menor = entrada
        
print(f"O maior número é {maior} e o menor é {menor}")