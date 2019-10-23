l1 = 0
s = 0;m = 0#soma e media
i = []#linha
c = []#coluna
lista = []
l = int(input())
if(l >= 0 and l <= 11):
    t = input().upper()
    for kj in range(12):
        for n in range(12):
            v = float(input())
            i.append(v)
        c.append(i)
        if(kj == l):
            lista = i
        i = []
    if('S' == t):
        for p in lista:
            s += p
        print(s)
    elif('M' == t):
        for p in lista:
            m += (p)
        m = m / 12
        print(m)
