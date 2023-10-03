nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

if nota1 < 0 or nota1 > 10:
    print("Nota Invalida")
    
elif nota2 < 0 or nota2 > 10:
    print("Nota Invalida")
    
elif nota3 < 0 or nota3 > 10:
    print("Nota Invalida")
    
else:
    print((nota1+nota2+nota3)/3)