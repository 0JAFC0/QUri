D = 2; I = 3
S = 0
S = 1 + I/D
while(I != 39):
    I = I + 2
    D = D * 2
    S += I/D
print("{:.2f}".format(S))
