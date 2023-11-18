def maior_fator_comum(a, b):
    while b:
        a, b = b, a % b
    return a

def simplificar_fração(numerador,denominador):
    if denominador==0:
        return "Erro, denominador não pode ser 0"
    mdc=maior_fator_comum(numerador,denominador)
    numeradorS=numerador//mdc
    denominadorS=denominador//mdc

    return numeradorS, denominadorS

numerador=int(input("Digite o valor para o númerador: "))
denominador=int(input("Digite o valor para o denominador: "))

resultado=simplificar_fração(numerador, denominador)

if type(resultado) == tuple:
    numeradorS, denominadorS = resultado
    print(f"A fração {numerador}/{denominador} simplificada é {numeradorS}/{denominadorS}.")
else:
    print(resultado)
