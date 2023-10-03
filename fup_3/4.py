#Faça um programa que leia 10 inteiros e imprima sua média.
med = 0


for i in range(0, 10):
    num = float(input(""))
    med += num
    
    
med /= 10
print(f"{med:.2f}")