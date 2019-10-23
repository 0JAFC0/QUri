n = int(input())
lista = []
for c in range(n):
    lista.append("Ho")
    l = " ".join(lista)
for il in range(15):
    if(len(lista) > 15):
        print("{}!".format(l))
    elif(len(lista) < 15):
        print("{}!".format(l))

