N = int(input())
for C in range(N):
    V  = int(input())
    if(V == 0):
        print("NULL")
    if(V > 0 and V % 2 == 0):
        print("EVEN POSITIVE")
    if(V % 2 != 0 and V > 0):
        print("ODD POSITIVE")
    if(V < 0 and V % 2 == 0):
        print("EVEN NEGATIVE")
    if(V < 0 and V % 2 != 0):
        print("ODD NEGATIVE")
