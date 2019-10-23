"""Arthur"""

DDD = int(input())
A = [61,71,11,21,32,19,27,31]
CI = ["Brasilia","Salvador","Sao Paulo","Rio de Janeiro","Juiz de Fora","Campinas","Vitoria","Belo Horizonte"]
C = 0
if(DDD in A):
    while(C < 8):
        if(DDD == A[C]):
            print(CI[C])
        C += 1
else:
    print("DDD nao cadastrado")

"""Dante

n = int(input())
a = [61,71,11,21,32,19,27,31]
b = ["Brasilia","Salvador","Sao Paulo","Rio de Janeiro","Juiz de Fora","Campinas","Vitoria","Belo Horizonte"]
c = 0
if n in a:
    while (c < 8):
        if (n == a[c]):
            print(b[c])
        c += 1
else:
    print("DDD nao cadastrado")
"""
