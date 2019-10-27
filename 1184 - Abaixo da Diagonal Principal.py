m = []
l = []
s = 0
con = 0

o = input().lower()
for a in range(12):
    for b in range(12):
        l.append(float(input()))
    m.append(l)
    l = []
c = 0
for i in range(len(m[0])):
    for x in range(c):
        s += m[i][x]
        con += 1
    c += 1
if(o == "s"):
    print(s)
else:
    if(o == "m"):
        print("{:.1f}".format(s / con))
