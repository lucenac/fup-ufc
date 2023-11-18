def divisao(dividendo, divisor):
    if divisor == 0:
        return 'Divisão por 0 não é permitida'
    quociente=0
    sinal=1

    if dividendo < 0:
        dividendo = - dividendo
        sinal= -sinal
    if divisor < 0:
        divisor = - divisor
        sinal=-sinal

    while dividendo >= divisor:
        dividendo -= divisor
        quociente+=1
    
    quociente*=sinal

    return quociente

dividendo =int (input(""))
divisor = int(input(""))


print(divisao(dividendo,divisor))