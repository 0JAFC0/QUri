a = []
con = 0
for i in range(1,21):
    n = int(input())
    a.append(n)
l = len(a)
a.reverse()
for c in a:
    print("N[{}] = {}".format(con, c))
    con += 1
