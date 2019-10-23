N = int(input())
for A in range(N):
    lista = []
    X = int(input())
    for C in range(1,X+1):
        if(X % C == 0):
            lista.append(C)
    if((len(lista) == 2) and (1 in lista) and (X in lista)):
        print("{} eh primo".format(X))
    else:
        print("{} nao eh primo".format(X))
