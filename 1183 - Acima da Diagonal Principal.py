m = []
l = []
soma = 0
i = 1;c = 0

o = input().upper()

for a in range(12):
    for b in range(12):
        n = float(input())
        l.append(n)
    m.append(l)
    l = []
for x in range(len(m[0])):
    for y in range(i, len(m[0])):
        soma += m[x][y]
        c += 1
    i += 1

if(o == "S"):
    print("{:.1f}".format(soma))
elif(o == "M"):
    print("{:.1f}".format(soma / c))
