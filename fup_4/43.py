idade_mais_jovem = float('inf')
idade_mais_velha = float('-inf')
nome_mais_jovem = None
nome_mais_velho = None

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break

    idade = int(input("Digite a idade da pessoa: "))

    if idade < 0:
        print("Idade negativa detectada. Encerrando o programa.")
        break

    if idade < idade_mais_jovem:
        idade_mais_jovem = idade
        nome_mais_jovem = nome

    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velho = nome

if nome_mais_jovem is not None and nome_mais_velho is not None:
    print(f"A pessoa mais jovem é {nome_mais_jovem} com {idade_mais_jovem} anos.")
    print(f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velha} anos.")
else:
    print("Nenhum dado inserido. O programa foi encerrado sem informações sobre idades.")
