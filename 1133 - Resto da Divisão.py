X = int(input())
Y = int(input())
if(X < Y):
    for C in range(X + 1, Y):
        if(C % 5 == 2 or C % 5 == 3):
            print(C)

else:
    for C in range(Y + 1, X):
        if(C % 5 == 2 or C % 5 == 3):
            print(C)
