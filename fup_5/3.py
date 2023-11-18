#Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. 
#Entre com um caractere (vogal ou consoante) e substitua todas as vogais da palavra dada por esse caractere.

def vogal(palavra):
    vogais="AEIOUaeiou"
    contador=0
    for letra in palavra:
        if letra in vogais:
            contador+=1
    return contador

palavra=input("Digite uma palavra: ")
vogais=vogal(palavra)

substituto=input("Digite um novo caractere para substituir as vogais: ")

nova_palavra=""

for letra in palavra:
    if letra in "AEIOUaeiou":
        nova_palavra+=substituto
    else:
        nova_palavra+=letra

print(f"{nova_palavra} essa é a nova palavara")
print(f"{vogais} número de vógais substituidas.")