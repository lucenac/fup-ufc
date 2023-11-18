def cifra_de_cesar(frase, deslocamento):
    nova_frase = ""
    
    for char in frase:
        if char.isalpha():
            if char.islower():
                limite_alfabeto = ord('z')
            else:
                limite_alfabeto = ord('Z')
            
            char_deslocado = ord(char) + deslocamento
            if char_deslocado > limite_alfabeto:
                char_deslocado -= 26

            nova_frase += chr(char_deslocado)
        else:
            nova_frase += char
    
    return nova_frase

frase = input("Digite a frase: ")
deslocamento = int(input("Digite o deslocamento: "))
nova_frase = cifra_de_cesar(frase, deslocamento)
print("Nova frase:", nova_frase)
