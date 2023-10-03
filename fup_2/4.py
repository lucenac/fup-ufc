def antsus(x):
    return x - 1, x + 1


num = input()
antecessor, sucessor = antsus(int(num))
print(antecessor, sucessor)