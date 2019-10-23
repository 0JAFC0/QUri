N = int(input())
for C in range(N):
    X, Y = str(input()).split()
    X = int(X); Y = int(Y)
    soma = 0
    if(X < Y and X % 2 == 0):
        for I in range(X+1, Y, 2):
            soma += I
    elif(X < Y and X % 2 != 0):
        for I in range(X+2, Y, 2):
            soma += I
    elif(Y < X and Y % 2 == 0):
        for I in range(Y+1, X, 2):
            soma += I
    elif(Y < X and Y % 2 != 0):
        for I in range(Y+2, X, 2):
            soma += I
    print("{}".format(soma))
