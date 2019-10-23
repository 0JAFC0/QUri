C = 0
D = 0
while True:
    N = int(input())
    if(N > 0):
        D += N
        C += 1
        media = D / C
    if(N < 0):
        break
print("{:.2f}".format(media))
