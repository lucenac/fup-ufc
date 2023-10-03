def valor(x):
    if x < 0:
        return - 1
    elif x == 0:
        return 0
    else:
        return 1
    
entrada = int(input())

print(valor(entrada))