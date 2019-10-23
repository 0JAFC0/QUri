c = int(input())
for i in range(c):
    n, f = str(input()).split()
    f = int(f);n = str(n).lower()
    if(f >= 1 and f <= 25000):
        if(n == "thor"):# o que importa é quem e não a força
            print("Y")
        else:
            print("N")
