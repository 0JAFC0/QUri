anterior = 0
for C in range(100):
    n = int(input())
    if(n > anterior):
        nmaior = n
        posição = C + 1
        anterior = n
print(nmaior)
print(posição)
