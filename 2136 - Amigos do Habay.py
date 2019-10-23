c = 0
p = 0
listay = []
listan = []
le = 0
while(c != 1):
    n = input().split()
    if("FIM" in n):
        c += 1
    if("YES" in n and n[0] not in listay):
        listay.append(n[0])
        
        if(len(n[0]) > le):
            le = len(n[0])
            ah = n[0]
    elif("NO" in n and n[0] not in listan):
        listan.append(n[0])
listay.sort()
listan.sort()
s = listay + listan
for i1 in s:
    print(i1)
print("\nAmigo do Habay:\n{}".format(ah))
