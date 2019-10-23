v = int(input())
if(v <= 50):
    lista = []
    lista.append(v)
    for ve in range(9):
        v *= 2
        lista.append(v)
    for x in lista:
        i = lista.index(x)
        print("N[{}] = {}".format(i, x))
