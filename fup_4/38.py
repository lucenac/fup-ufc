def sao_strings_iguais(string1, string2):
    if len(string1) != len(string2):
        return False 

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False  

    return True
string1 = input("")
string2 = input("")

if sao_strings_iguais(string1, string2):
    print("As strings são iguais.")
else:
    print("As strings são diferentes.")
