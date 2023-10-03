def split(x):
    p = x * 46/100
    s = x * 32/100
    t = x * 22/100
    return p, s, t


entrada = float(input())

primeiro, segundo, terceiro = split(entrada)

print(f'{primeiro:.2f} {segundo:.2f} {terceiro:.2f}')