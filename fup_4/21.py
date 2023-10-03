def maior(x,y):
    if x > y:
        return f'{x} é maior que {y}'
    elif x == y:
        return f'{x} é igual a {y}'
    else:
        return f'{x} é menor que {y}'
    
x = int(input())
y = int(input())

print(maior(x,y))