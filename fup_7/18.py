#Faça uma função que receba dois vetores, A e B, de mesmo tamanho. Crie um novo vetor
# denominado C calculando C = A – B (a diferença elemento a elemento). Retorne o vetor C.
def dif_vet(A, B):
    return [a - b for a, b in zip(A, B)]

vet_A = [int(input(f"Vetor A, valor {i + 1}: ")) for i in range(0, 5)]
vet_B = [int(input(f"Vetor B, valor {i + 1}: ")) for i in range(0, 5)]

vet_C = dif_vet(vet_A, vet_B)
print("Vetor C (A - B):", vet_C)