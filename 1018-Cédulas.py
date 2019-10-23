N = float(input())
N += 0.001
Total = N
Notas = 100.00
Tonotas = 0
while True:
    if(Total >= Notas):
        Total -= Notas
        Tonotas += 1
    else:
        print("{} nota(s) de R$ {:.0f},00".format(Tonotas, Notas))
        if(Notas == 100):
            Notas = 50
            Tonotas = 0
        elif(Notas == 50):
            Notas = 20
            Tonotas = 0
        elif(Notas == 20):
            Notas = 10
            Tonotas = 0
        elif(Notas == 10):
            Notas = 5
            Tonotas = 0
        elif(Notas == 5):
            Notas = 2
            Tonotas = 0
        elif(Notas == 2):
            Notas = 1
            Tonotas = 0
        elif(Notas == 1):
            Notas = 0
            Tonotas = 0
        if(Total == 0):
            break
