def saque(x):
    cem = x // 100
    x %= 100
    
    cinq = x // 50
    x %= 50
    
    vint = x // 20
    x %= 20
     
    dez = x // 10
    x %= 10
     
    cinc = x // 5
    x %= 5
     
    dois = x // 2
    x %= 2
     
    um = x
    
    return cem, cinq, vint, dez, cinc, dois, um

entrada = int(input())

cedulas = saque(entrada)

print(f'{cedulas[0]}') 
print(f'{cedulas[1]}') 
print(f'{cedulas[2]}') 
print(f'{cedulas[3]}') 
print(f'{cedulas[4]}') 
print(f'{cedulas[5]}') 
print(f'{cedulas[6]}') 