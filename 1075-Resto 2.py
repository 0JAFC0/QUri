N = int(input())
c = 0
for C in range(10000):
    resto = C % N
    if(resto == 2):
        print(C)
