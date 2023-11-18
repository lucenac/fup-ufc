#Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais
def vogal(caractere):
    return caractere in "AEIOUaeiou"
string=input("")

resultado = ""
for caracatere in string:
    if not vogal(caracatere):
        resultado+=caracatere

print(resultado)