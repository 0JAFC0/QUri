x = float(input())
lista = []
lista.append(x)
for c in range(1,100):
    x /= 2
    lista.append(x)
for x1 in lista:
    y = lista.index(x1)
    print("N[{}] = {:.4f}".format(y, x1))
    
