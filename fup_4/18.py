def data(x):
    #formatar o dia
    d2 = x[1]
    if int(x[0]) > 0:
        d1 = x[0]
    else:
        d1=''
    dia = d1+d2
    
    #mes
    m2 = x[4]
    if int(x[3]) > 0:
        m1 = x[3]
    else:
        m1=''
        
    m = m1+m2
    int_m = int(m)
    if int_m == 1:
        mes = 'janeiro'
    elif int_m == 2:
        mes = 'fevereiro'
    elif int_m == 3:
        mes = 'março'
    elif int_m == 4:
        mes = 'abril'
    elif int_m == 5:
        mes = 'maio'
    elif int_m == 6:
        mes = 'junho'
    elif int_m == 7:
        mes = 'julho'
    elif int_m == 8:
        mes = 'agosto'
    elif int_m == 9:
        mes = 'setembro'
    elif int_m == 10:
        mes = 'outubro'
    elif int_m == 11:
        mes = 'novembro'
    elif int_m == 12:
        mes = 'dezembro'
    else:
        return 'Mês invalido'
    
    #ano
    ano = x[6:10]
    return f"{dia} de {mes} de {ano}"


entrada = input()
print(data(entrada))