N = int(input())
for C in range(N):
    X, Y = str(input()).split()
    X = int(X); Y = int(Y)
    if(Y == 0):
        print("divisao impossivel")
    else:
        d = X / Y
        print("{:.1f}".format(d))
