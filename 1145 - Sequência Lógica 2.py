X, Y = str(input()).split()
X = int(X); Y = int(Y)
l = 0
lista = []
for C in range(1,Y+1):
    lista.append(C)
    if(len(lista) == X):
        print(" ".join(map(str, lista)))
        lista = []
