for c in range(3):
    l = int(input())
    maior = 0
    if(l >= 1 and l <= 500):
        v = str(input()).split()
        for vi in v:
            vi = int(vi)
            if(vi > maior):
                maior = vi
        if(maior < 10):
            print("1")
        elif(maior >= 10 and maior < 20):
            print("2")
        elif(maior >= 20):
            print("3")
