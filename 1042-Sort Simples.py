A, B, C = str(input()).split()
A = int(A); B = int(B); C = int(C)
if(A < B and A < C):
    m1 = A
elif(B < A and B < C):
    m1 = B
elif(C < A and C < B):
    m1 = C
if(A > B and A > C):
    m2 = A
elif(B > A and B > C):
    m2 = B
elif(C > A and C > B):
    m2 = C
#analisando m3
if(m1 == B and m2 == C):
    m3 = A
elif(m1 == C and m2 == B):
    m3 = A
elif(m1 == A and m2 == C):
    m3 = B
elif(m1 == C and m2 == A):
    m3 = B
elif(m1 == A and m2 == B):
    m3 = C
elif(m1 == B and m2 == A):
    m3 = C
print(m1)
print(m3)
print("{}\n".format(m2))

print(A)
print(B)
print(C)
