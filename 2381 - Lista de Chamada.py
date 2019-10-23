# ela colocou N pedaços de papel numerados de 1 a N em um saquinho
# sorteou um determinado número K
n, k = str(input()).split()
n = int(n);k = int(k)
lista = []
for c in range(n):
    ca = str(input()).lower()
    lista.append(ca)
o = lista.sort()
print(lista[k-1])
