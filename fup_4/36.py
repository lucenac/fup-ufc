def primo(n):
    if n<=1:
        return None
    fator=2
    while n>1:
        if n% fator==0:
            n//=fator
        else:
            fator+=1
    return fator

n = int(input(""))
resultado=primo(n)

if primo(n):
    print(f"O maior fator primo de {n} é {resultado}")
else:
    print(f"{n} não tem fatores primos")