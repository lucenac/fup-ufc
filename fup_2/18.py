def prem(a,b,c, vp):
    vt = a + b + c
    iv1 = (a / vt) * vp
    iv2 = (b / vt) * vp
    iv3 = (c / vt) * vp
    return iv1, iv2, iv3
    
    
iv1 = float(input())
iv2 = float(input())
iv3 = float(input())

vp = float(input())

p1, p2, p3 = prem(iv1, iv2, iv3, vp)
print(f'{p1:.2f} {p2:.2f} {p3:.2f}')