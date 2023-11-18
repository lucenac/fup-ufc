def contar(string):
    contar=0
    for char in string:
        if char=='1':
            contar+=1
    return contar

string=input("")
numero_de_uns=contar(string)

print({numero_de_uns})