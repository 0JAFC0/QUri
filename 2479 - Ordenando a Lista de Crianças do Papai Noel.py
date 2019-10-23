n = int(input())
lista = []
comp = 0
ncomp = 0
for i in range(n):
    n1 = input().split()
    lista.append(n1[1])
    if("+" in n1):
        comp += 1
    else:
        ncomp += 1
lista.sort()    
for c in lista:
    print(c)
print("Se comportaram: {} | Nao se comportaram: {}".format(comp, ncomp))
