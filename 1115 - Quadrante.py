X = 1; Y = 1
while(X != 0 or Y != 0):
    X, Y = str(input()).split()
    X = int(X); Y = int(Y)
    if(Y > 0 and X > 0):
        print("primeiro")
    elif(Y > 0 and X < 0):
        print("segundo")
    elif(Y < 0 and X < 0):
        print("terceiro")
    elif(Y < 0 and X > 0):
        print("quarto")
