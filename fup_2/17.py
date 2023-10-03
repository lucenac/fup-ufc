from math import sqrt

def dist(x,y):
    d = sqrt(x**2+y**2)
    return d

x = int(input())
y = int(input())

print(f'{dist(x,y):.2f}')