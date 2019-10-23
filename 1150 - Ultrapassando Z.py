contx = 0; cont = 0
x = int(input())
z = int(input())
while(z <= x):
    z = int(input())
while(contx < z):
    if(cont == 0):
        contx += x
    else:
        x += 1
        contx += 1
    cont += 1
print(cont)
