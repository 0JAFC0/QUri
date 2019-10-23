while True:
    N = int(input())
    A = 0
    lista = []
    if(N == 0):
        break
    else:
        while(len(lista) != 5):
            if(N % 2 == 0):
                lista.append(N)
                N += 2
            else:
                N += 1
        print(sum(lista))

