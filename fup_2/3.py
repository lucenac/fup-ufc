def ape(x,y):
    area = x * y
    perimetro = 2*x + 2*y
    return area, perimetro
    
l1 = float(input())
l2 = float(input())

area, perimetro = ape(l1, l2)

print(area, perimetro)