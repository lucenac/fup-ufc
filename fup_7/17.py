# Faça uma função que receba um vetor e um número inteiro x e
# retorne os múltiplos do número x que existem no vetor.
def mul_x(v, x):
    return [num for num in v if num % x == 0]

vetor = [int(input(f"Valor {i + 1}: ")) for i in range(0, 10)]
x = int(input("Número inteiro x: "))

resultado = mul_x(vetor, x)
print(f"Múltiplos de {x}:", resultado)