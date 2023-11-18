'''Faça um função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no
formato textual por extenso. Exemplo: Data: 01/01/2000, imprimir: 1 de janeiro de 2000.'''
def data_form(entrada): 
    if len(entrada) != 10 or entrada[2] !='/' or entrada[5] !='/': 
        return 'A entrada deve ser no formato AA/MM/AAAA'
    
    dia = ''
    mes = ['janeiro','fevereiro','março', 'abril', 'maio', 'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']
    ano = ''
    cont_mes = ''
    cont = 0

    for num_dia in entrada:
        if num_dia == '/':
            break
        dia += num_dia
        
    for num_mes in entrada:
        cont+=1
        if cont > 3 and cont < 6:
            cont_mes += num_mes
        if cont > 5:
            cont = 0
            break
        
    for num_ano in entrada:
        cont += 1
        if cont > 6:
            ano += num_ano

            
    if not dia.isdigit() or not cont_mes.isdigit() or not ano.isdigit():
        return 'Dia, mês e ano devem ser números.'
        
    dia = int(dia)
    cont_mes = int(cont_mes)
    ano = int(ano)
        
    if not (1<= dia <= 31) or not (1<=cont_mes<=12) or not(1000<=ano<=9999):
        return 'Dia, mês e ano estão fora dos intervalos válidos'

    return f'{dia} de {mes[cont_mes - 1]} de {ano}'

entrada = input('Insira uma data(DD/MM/AAAA):')
print(data_form(entrada))