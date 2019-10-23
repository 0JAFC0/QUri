a, b, A, B = str(input()).split()
a = int(a)
b = int(b)
A = int(A)
B = int(B)
if (A - a == 1 and b > B):# 
    s = 60 - b
    m = s + B
    h = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
elif(a < A and b < B):#ver se a Hora inicial é maior que a hora final e se o minuto inicial é menor que o minuto final
    h = A - a
    m = B - b
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
elif(a == A and b < B):#
    h = 0
    m = B - b
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
elif(a < A and b > B):#
    h = (A - a) - 1
    a = 60 - b
    m = a + B
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
elif(a == A and b == B):# se o tempo é igual
    h = 24
    m = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))    
elif(a > A):#se a hora inicial é maior que a final
    h = (24 - a) + A
    m = B - b
    if(b > B):# se o minuto inicial é maior que o final
        h = h - 1
        m = (60-b) + B
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))    
    else:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
