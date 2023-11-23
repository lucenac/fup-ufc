# Faça uma função que receba dois vetores de mesmo tamanho e calcule outro vetor contendo, nas
# posições pares o valores do primeiro vetor e nas posições ímpares os valores do segundo vetor.
def intercal(v1, v2):
    return [val for t in zip(v1, v2) for val in t]

v1 = [int(input(f"Vetor A, valor {i + 1}: ")) for i in range(0, 5)]
v2 = [int(input(f"Vetor B, valor {i + 1}: ")) for i in range(0, 5)]

vc = intercal(v1, v2)
print("Vetor C:", vc)