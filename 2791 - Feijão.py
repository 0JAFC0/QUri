copos = input().split()
for c in range(4):
    copos[c] = int(copos[c])
    if(copos[c] == 1):
        print(c+1)
