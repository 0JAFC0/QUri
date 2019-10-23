M = 1; N = 1;lista = []
S = 0
while(M != 0 or N != 0):
    M, N = str(input()).split()
    M = int(M); N = int(N)
    if(M < N):
        A = M
    elif(N < M):
        A = N
    if(M > N):
        B = M
    elif(N > M):
        B = N
    if(M == 0 or N == 0 or M < 0 or N < 0):
        break
    if(M == N):
        A = M
        B = N
    lista.append(A)
    S += A
    while(A < B):
        A += 1
        S += A
        lista.append(A)
        l = " ".join(map(str, lista))
    l = " ".join(map(str, lista))
    print("{} Sum={}".format(l, S))
    lista = []
    S = 0; A = 0; B = 0
