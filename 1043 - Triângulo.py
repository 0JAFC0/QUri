A, B, C = str(input()).split()
A = float(A);B = float(B);C = float(C)
if(A < B + C and B < A + C and C < A + B):
    P = A + B + C  
    print("Perimetro = {:.1f}".format(P))
else:
    Areat = ((A + B) * C) / 2
    print("Area = {:.1f}".format(Areat))
