lista = []

for i in range(10):
    entrada = int(input('Insira um valor: '))
    lista.insert(0, entrada)
    
for item in lista:
    print(item)