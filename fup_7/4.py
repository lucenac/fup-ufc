lista = []

for i in range(10):
    entrada = input('Insira um valor: ')
    lista.insert(0, int(entrada))
    
for item in lista:
    print(item)