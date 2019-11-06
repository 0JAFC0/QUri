n, m = map(int, input().split())
while(n != 0 and m != 0):
    l = []
    s = 0
    s = n + m
    
    s = str(s)
    for c in range(len(s)):
        if(not s[c] == "0"):
            l.append(s[c])
    s = ""
    for a in range(len(l)):
        s += l[a]
    
    print(s)
    n, m = map(int, input().split())
