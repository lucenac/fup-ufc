def inverter(x):
    c = x // 100
    d = (x // 10) % 10
    u = x % 10
    return u, d, c
entrada = int(input())

u, d, c = inverter(entrada)

print(f'{u}{d}{c}')