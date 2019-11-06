def linguas(pe):
    l = []
    ld = []
    li = []
    for b in range(pe):
        l.append(input())
    for i in range(1,len(l)):
        if(l[0] != l[i]):
            ld.append(l[i])
        else:
            li.append(l[i])
            
    if(len(ld) > 0):
        for c in range(len(ld)):
            return "ingles"
    elif(len(li) > 0):
        return li[0]
n = int(input())
for a in range(n):
    pe = int(input())
    print(linguas(pe))
