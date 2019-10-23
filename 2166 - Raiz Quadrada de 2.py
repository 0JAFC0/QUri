
for c in range(1):
    t = int(input())
    r = t - 2015
    if(r > 0):
        print("{} A.C.".format(r+1))
    elif(r < 0):
        print("{} D.C.".format(r))
    else:
        print("{} A.C".format(r))
