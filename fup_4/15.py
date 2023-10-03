entrada = int(input())
cont = 0

for i in range(1, entrada):
    if entrada % i == 0:
        cont += i
        
print(cont)