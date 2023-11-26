import random

def apresentar_matriz (x):
    for l in range(len(x)):
        for c in range(len(x)):
            print(f"{x[l][c]}\t", end = "")
        print()

def modificando_matriz(lista):
    lista[0][1] = 0
    lista[0][2] = 0
    lista[0][3] = 0
    lista[0][4] = 0
    lista[1][2] = 0
    lista[1][3] = 0
    lista[1][4] = 0
    lista[2][3] = 0
    lista[2][4] = 0
    lista[3][4] = 0

    return lista

pergunta = "S"
while pergunta == "S":
    num = int(input("Digite um valor para a semente: "))
    random.seed(num)
    
    matriz = []
    for linha in range(5):
        linh = []
        for coluna in range(5):
            linh.append(random.randint(1,20))
        matriz.append(linh)
    
    print("/" * 30)
    print("A matriz gerada pela semente:")
    print(apresentar_matriz(matriz))

    matriz_diagonal_superior_zero = modificando_matriz(matriz)
    print("/" * 30)
    print("A matriz final:")
    print(apresentar_matriz(matriz_diagonal_superior_zero))

    pergunta = input("Gostaria de continuar? [S/N] ").upper()
print("Finalizando progama...")

"""
(0,0)#  (0,1)   (0,2)   (0,3)   (0,4)
(1,0)   (1,1)#  (1,2)   (1,3)   (1,4)   
(2,0)   (2,1)   (2,2)#  (2,3)   (2,4)   
(3,0)   (3,1)   (3,2)   (3,3)#  (3,4)   
(4,0)   (4,1)   (4,2)   (4,3)   (4,4)#  

superior = (0,1)   (0,2)   (0,3)   (0,4)  (1,2)   (1,3)   (1,4)  (2,3)   (2,4)  (3,4)  




"""