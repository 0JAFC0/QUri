m = []
l = []
s = 0;c = 0
con = 11

o = input().lower()
for a in range(12):
    for b in range(12):
        l.append(float(input()))
    m.append(l)
    l = []

for i in range(len(m[0])-1):
    for x in range(con):
        s += m[i][x]
        c += 1
    con -= 1
    
if(o == "s"):
    print(s)
elif(o == "m"):
    print("{:.1f}".format(s / c))
