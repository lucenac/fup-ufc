def eh_palindromo(string):
    string=string.replace("", "").lower()
    return string==string[::-1]
frase=input("")
if eh_palindromo(frase):
    print(f"{frase} é um palindromo")
else:
    print("Não é um palindromo")