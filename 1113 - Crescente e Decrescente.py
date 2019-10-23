X = 1; Y = 2
while X != Y:
    X, Y = str(input()).split()
    X = int(X); Y = int(Y)
    if(X > Y):
        print("Decrescente")
    if(Y > X):
        print("Crescente")
