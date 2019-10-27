cq = 0

n = int(input())
for a in range(n):
    l, c = map(int, input().split())
    if(l, c >= 0 and l, c <= 100):
        if(l > c):
            cq += c
        
print(cq)
