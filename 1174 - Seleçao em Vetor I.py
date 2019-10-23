lista = []
i = 0
for c in range(100):
    a = float(input())
    lista.append(a)
    if(a <= 10):
        print("A[{}] = {}".format(i, a))
    i += 1
