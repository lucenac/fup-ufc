def update(x):
    x += x * 21.37/100
    return x


entrada = float(input())
print(f'{update(entrada):.2f}')