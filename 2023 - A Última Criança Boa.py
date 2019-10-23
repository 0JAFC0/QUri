lista = []
while True:
    try:
        n = str(input())
        lista.append(n)
        lista.sort()
    except EOFError:
        break
