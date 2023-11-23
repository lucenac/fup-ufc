# Leia 10 números inteiros e armazene em um vetor. Em seguida escreva
# os elementos que são primos e suas respectivas posições no vetor.
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

v = [int(input(f"Valor posição {i + 1}: ")) for i in range(10)]

print("Primos e posições:")
for i, num in enumerate(v):
    if primo(num):
        print(f"Posição {i + 1}: {num}")