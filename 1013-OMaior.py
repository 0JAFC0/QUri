A, B, C = str(input()).split()
A = int(A)
B = int(B)
C = int(C)
if(A > B and A > C):
    Maior = A
else:
    if(B > A and B > C):
        Maior = B
    elif(C > A and C > B):
        Maior = C
print("{} eh o maior".format(Maior))
