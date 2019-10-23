p = 0
for c in range(5):
    n = int(input())
    par = n % 2
    if(par == 0):
        p += 1
print("{} valores pares".format(p))
