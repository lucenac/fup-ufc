entrada= input('Quantas questões você quer gerar? ')

for i in range(1,int(entrada)+1):
    nome_arquivo = f'{i}.py'
    with open(nome_arquivo,"w"):
        pass