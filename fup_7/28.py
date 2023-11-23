# Faça um programa para ler 12 inteiros DIFERENTES a serem armazenados em um vetor.
# Os dados deverão ser armazenados na ordem que forem sendo lidos, mas caso o usuário
# digite um número que já foi digitado anteriormente, o programa deverá pedir para ele
# digitar outro número. Exibir na tela o vetor final que foi digitado.
def leitura():
    vetor = []
    for i in range(0, 12):
        while True:
            num = int(input("Numero:"))
            if num not in vetor:
                vetor.append(num)
                break
            else:
                print("Digite outro numero.")

    return vetor

vf = leitura()
print("Vetor final:", vf)