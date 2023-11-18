def palavra_mais_cedo(palavra1, palavra2):
    i = 0
    while i < len(palavra1) and i < len(palavra2):
        if palavra1[i] < palavra2[i]:
            return palavra1
        elif palavra1[i] > palavra2[i]:
            return palavra2
        i += 1
    if len(palavra1) < len(palavra2):
        return palavra1
    else:
        return palavra2

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

resultado = palavra_mais_cedo(palavra1, palavra2)

print("A palavra que vem primeiro na ordem alfabética é:", resultado)
