def spliter(x):
    m = x // 1000
    c = x // 100 % 10
    d = x // 10 % 10
    u = x % 10
    return m, c, d, u


entrada = int(input())
m, c, d, u = spliter(entrada)
print(m, c, d, u)