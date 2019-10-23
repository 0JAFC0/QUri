nota = 0; m = 0; op = 1
while(op == 1):
    while(nota < 2):
        N = float(input())
        if(N < 0.0 or N > 10.0):
            print("nota invalida")
        if(N >= 0.0 and N <= 10.0):
            nota += 1
            m += N
    print("media = {:.2f}".format(m/2))
    while True:
        op = int(input("novo calculo (1-sim 2-nao)\n"))
        nota = 0; m = 0
        if(op == 1 or op == 2):
            break
