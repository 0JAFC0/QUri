a, b, A, B = str(input()).split()
a = int(a)
b = int(b)
A = int(A)
B = int(B)
if (a > b):
    s = 24 - a
    h = s + b
    print("O JOGO DUROU {} HORA(S)".format(h))
else:
    if(b > a):
        h = b - a
        print("O JOGO DUROU {} HORA(S)".format(h))
    else:
        if(a == b):
            h = 24
            print("O JOGO DUROU {} HORA(S)")
