def contar_caracteres_brancos(frase):
    count = 0
    for char in frase:
        if char == ' ' or char == '\t' or char == '\n' or char == '\r' or char == '\f' or char == '\v':
            count += 1
    return count

frase = input("Digite uma frase: ")
num_caracteres_brancos = contar_caracteres_brancos(frase)

print(f"O número de caracteres brancos na frase é: {num_caracteres_brancos}")
