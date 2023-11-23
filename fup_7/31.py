# Digite um nome e imprima quantas letras diferentes tem esse nome.
def cont(nome):
    led = list(set(nome))
    return len(led)

nome = input("Digite um nome: ")

qled = cont(nome)
print(f"O nome '{nome}' possui {qled} letras diferentes.")