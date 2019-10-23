N = int(input())
A = 0
n1 = 0
n2 = 1
lista = []
for C in range(N):
##    print(n1,end=" ")
    lista.append(n1)
    A = n1 + n2
    n1 = n2
    n2 = A
    l = " ".join(map(str, lista))
print(l) 
