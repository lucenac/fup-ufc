def conversor(x):
    h = x // 3600
    m = (x % 3600) // 60
    s = x % 60
    return h, m, s

entrada = int(input())

h, m, s = conversor(entrada)
print(h, m, s)