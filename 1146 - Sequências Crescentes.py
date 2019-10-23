while True:
    lista = []
    X = int(input())
    if(X == 0):
        break
    else:
        for I in range(1,X+1):
            lista.append(I)
        print(' '.join(map(str, lista)))
