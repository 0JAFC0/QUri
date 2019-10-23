X = int(input())
Y = int(input())
soma = 0
if(X > Y):
    a = Y; b = X
if(X <= Y):
    a = X; b = Y
while(a <= b):
    if(a % 13 != 0):
        soma += a
    a += 1
print(soma)
