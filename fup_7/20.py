# Faça um programa que leia um vetor de 100 posições para números reais e, depois, um código inteiro.
# Se o código for 0, finalize o programa; se o código for 1, mostre o vetor na ordem direta; se for 2,
#mostre o vetor na ordem inversa. Caso, o código seja diferente de 1 e 2 escreva uma mensagem informando
# que o código é inválido. O programa sempre deve pedir outro código, e terminar somente quando o código for 0.
def exibir(v, ordem):
    if ordem == 1:
        print("Vetor:", v)
    elif ordem == 2:
        print("Vetor inverso:", v[::-1])
    else:
        print("Inválido.")

vetor = [float(input(f"Valor posição {i + 1}: ")) for i in range(0, 100)]

while True:
    codigo = int(input("Código (1 para direto, 2 para inverso, 0 para sair): "))

    if codigo == 0:
        print("Fim do programa.")
        break
    elif codigo == 1 or codigo == 2:
        exibir(vetor, codigo)
    else:
        print("Inválido.")