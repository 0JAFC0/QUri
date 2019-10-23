N = int(input())
in1 = 0
out = 0
for C in range(N):
    X = int(input())
    if(X >= 10 and X <= 20):
        in1 += 1
    else:
        out += 1
print("{} in".format(in1))        
print("{} out".format(out))
