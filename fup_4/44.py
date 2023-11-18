def inverter_frase(frase):
    frase_invertida=frase[::-1]
    frase_modificada=""

    for letra in frase_invertida:
        if letra.lower()=="a":
            frase_modificada+="*"
        else:
            frase_modificada+=letra

    return frase_modificada

frase=input("")
frase_nova=inverter_frase(frase)
print(frase_nova)