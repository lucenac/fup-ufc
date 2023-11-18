def substituir_zero_por_um(string):
    nova_string = ""
    for char in string:
        if char == '0':
            nova_string += '1'
        else:
            nova_string += char
    return nova_string

string = input("Digite uma string contendo '0' para substituir por '1': ")
string_modificada = substituir_zero_por_um(string)
print(f"A string modificada é: {string_modificada}")
