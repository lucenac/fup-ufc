def perf(n):
    if n <= 0:
        return False
    soma_divisores=0

    for i in range(1, n):
        if n % i == 0:
            soma_divisores+=i
    return soma_divisores

n = int(input(""))
if perf(n):
    print(f"{n} é perfeito")
else:
    print(f"{n} não é perfeito")
