media = 0
positivo = 0
for C in range(6):
    n = float(input())
    if(n > 0):
        positivo += 1
        media += n
media = media / positivo
print("{} valores positivos".format(positivo))
print("{:.1f}".format(media))
