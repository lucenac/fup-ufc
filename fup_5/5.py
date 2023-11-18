"""Dados três valores inteiros, A , B e C, verificar se eles podem ser valores dos lados de um
triângulo e, se forem, verificar se é um triângulo escaleno, equilátero ou isósceles,
considerando os seguintes conceitos:
◦ O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
◦ Chama-se equilátero o triângulo que tem três lados iguais.
◦ Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
◦ Recebe o nome de escaleno o triângulo que tem três lados diferentes."""

def triangulo(A,B,C):
    if A<=0 or B<=0 or C<=0:
        return "Não é um triangulo."
    if (A+B > C) and (A+C> B) and (B+C>A):
        if A==B==C:
            return "Triangulo Equilátero."
        elif A==B or A==C or B==C:
            return "Triangulo Isóceles."
        else:
            return "Triangulo Escaleno"
    else:
        return "Não é um triangulo."

    
A=float(input("Digite um valor para um dos lados de um triangulo: "))
B=float(input("Digite outro valor para o segundo lado de um triangulo: "))
C=float(input("Digite o terceiro valor para o último lado: "))

resultado=triangulo(A,B,C)

print(resultado)