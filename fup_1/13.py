numero = int(input("Digite um número inteiro de três dígitos (entre 100 e 999): "))


if 100 <= numero <= 999:
    centenas = numero // 100
    dezenas = (numero // 10) % 10
    unidades = numero % 10

    numero_invertido = unidades * 100 + dezenas * 10 + centenas

    print(f"O número invertido é: {numero_invertido}")
else:
    print("O número deve estar no intervalo de 100 a 999.")
