N = int(input())
for A in range(N):
    soma=0
    X = int(input())
    for C in range(1,X):
        if(X % C == 0):
            soma += C
    if(soma==X):
        print("{} eh perfeito".format(X))
    else:
        print("{} nao eh perfeito".format(X))
