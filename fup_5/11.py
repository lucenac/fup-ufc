"""Faça uma função que receba uma cadeia de caracteres no formato “DD/MM/AAAA” e retorne o dia, mês e ano para 3 variáveis inteiras. 
Nessa função, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos.
Caso alguma verificação não seja válida, os retornos devem ser iguais a zero."""

def extrair_data(data_str):
    dia, mes, ano = 0, 0, 0
    partes = data_str.split('/')
    formato_correto=len(partes)==3 and data_str[2] == '/' and data_str[5] == '/'

    dia_eh_numero = partes[0].isdigit()
    mes_eh_numero = partes[1].isdigit()
    ano_eh_numero = partes[2].isdigit()

    dia = int(partes[0]) if dia_eh_numero else 0
    mes = int(partes[1]) if mes_eh_numero else 0
    ano = int(partes[2]) if ano_eh_numero else 0

    data_valida = (
        formato_correto and
        1 <= dia <= 31 and
        1 <= mes <= 12 and
        ano >= 1000
    )
    if not data_valida:
        dia, mes, ano = 0, 0, 0
    return dia, mes ,ano

data=input("Insira uma data no formato DD/MM/AAAA: ")

dia, mes, ano=extrair_data(data)

if dia == 0:
    print("Formato de data incorreto ou dia não numérico.")
elif mes == 0:
    print("Mês não numérico ou fora dos limites aceitáveis.")
elif ano == 0:
    print("Ano não numérico ou fora dos limites aceitáveis.")
else:
    print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")