"""Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. 
As condições para aposentadoria são:
◦ Ter pelo menos 65 anos;
◦ Ou ter trabalhado pelo menos 30 anos;
◦ Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos"""

idade=int(input("Digite a idade do trabalhador: "))
tempo_de_serviço=int(input("Quantos anos ele serviu: "))
if idade>=65 or tempo_de_serviço >=30 or (idade>=60 and tempo_de_serviço >=25):
    print("O trabalhador pode se aposentar")
else:
    print("O trabalhador não pode se aposentar")