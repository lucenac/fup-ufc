def med(x,y,z,op):
    if op == 'A':
        media = (x+y+z) / 3
        return media
    elif op == 'P':
        media = ((x * 5) + (y * 3) + (z * 2)) / 10
        return media
    else:
        return 'Insira uma opção válida!'
    
x = float(input())
y = float(input())
z = float(input())
op = input()

print(med(x,y,z,op))