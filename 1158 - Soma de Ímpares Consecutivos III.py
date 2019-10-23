N = int(input())
for C in range(N):
    S = 0
    Y = 0
    X, Y = map(int, input().split())
    lista = []
    
    while(len(lista) != Y):
        if(X % 2 == 0):
            X += 1
        else:
            lista.append(X)
            X += 2
    print(sum(lista))
