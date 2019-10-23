##def fib(a1):
##    if(a1 == 0 or a1 == 1):
##        return a1
##    else:
##        return fib(a1 - 1) + fib(a1 - 2)

t = int(input())
for c in range(t):
    a1 = 1
    a2 = 1
    lista = []
    n = int(input())
    if(n >= 0 and n <= 60):
            if(n == 0 or n == 1):
                lista = 0
            else:
                lista.append(a1)
                for i in range(0,n-1):
                    a = a1 + a2
                    a1 = a2
                    a2 = a
                    l = lista.append(a)
            print("Fib({}) = {}".format(n, lista[i]))
