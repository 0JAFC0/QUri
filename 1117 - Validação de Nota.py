nota = 0; m = 0
while nota != 2:
    N = float(input())
    if(N >= 0 and N <= 10):
        nota += 1
        m += N
    else:
        print("nota invalida")
media = m / nota
print("media = {:.2f}".format(media))
