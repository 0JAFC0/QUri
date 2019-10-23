X = int(input())
if(X % 2 == 0):
    impar = X +1
else:
    impar = X + 2
for c in range(6):
    print(impar)
    impar += 2
