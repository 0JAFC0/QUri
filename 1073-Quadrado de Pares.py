N = int(input())
if(N >= 5 and N <= 2000):
    for C in range(2, N+1, 2):
        q = C ** 2
        print("{}^2 = {}".format(C, q))
