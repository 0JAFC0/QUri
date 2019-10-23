lista = []
i = 0
for con in range(10):
    x1 = int(input())
    lista.append(x1)
for c in lista:
    if(c <= 0):
        i1 = lista.index(c)
        lista[i1] = 1
for x in lista:
    print("X[{}] = {}".format(i, x))
    i += 1
