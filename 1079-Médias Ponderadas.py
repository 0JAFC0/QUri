n = int(input())
for c in range(n):
    v1, v2, v3 = str(input()).split()
    v1 = float(v1); v2 = float(v2); v3 = float(v3)
    mediap = ((v1*2)+(v2*3)+(v3*5))/(2+3+5)
    print("{:.1f}".format(mediap))
    (6.4*2)+(4.3*3)+(6.2*5)/(2+3+5)
