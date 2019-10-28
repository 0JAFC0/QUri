m = []
l = []
s = 0;con = 0
c1 = 1
c2 = 11

o = input().lower()
for a in range(12):
    for b in range(12):
        l.append(float(input()))
    m.append(l)
    l = []

for i in range(len(m)):
    for x in range(c1, c2):
        s += m[i][x]
        con += 1
    c1 += 1
    c2 -= 1
if(o == "s"):
    print("{:.1f}".format(s))
elif(o == "m"):
    print("{:.1f}".format(s / con))
