c = int(input())
for l in range(c):
    n = int(input())
    if(100 <= n <= 100000):
        if(n <= 8000):
            print("Inseto!")
        elif(n > 8000):
            print("Mais de 8000!")
