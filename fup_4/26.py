maior = float('-inf') 
menor = float('inf')

for i in range(0, 10):
    entrada = int(input())
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada
print(f"O maior número é {maior} e o menor número é {menor}...")
     