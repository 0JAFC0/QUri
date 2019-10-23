N = float(input())
Total = N
Total = Total + 0.001
Notas = 100.00
Tonotas = 0
while True:
    if(Total >= Notas):
        Total -= Notas
        Tonotas += 1
    else:
        if(Notas == 100):
            print("Notas:")
            print("{} nota(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 50
            Tonotas = 0
        elif(Notas == 50):
            print("{} nota(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 20
            Tonotas = 0
        elif(Notas == 20):
            print("{} nota(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 10
            Tonotas = 0
        elif(Notas == 10):
            print("{} nota(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 5
            Tonotas = 0
        elif(Notas == 5):
            print("{} nota(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 2
            Tonotas = 0
        elif(Notas == 2):
            print("{} nota(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 1
            Tonotas = 0
        elif(Notas == 1):
            print("MOEDAS:")
            print("{} moedas(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 0.50
            Tonotas = 0
        elif(Notas == 0.50):
            print("{} moedas(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 0.25
            Tonotas = 0
        elif(Notas == 0.25):
            print("{} moedas(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 0.10
            Tonotas = 0
        elif(Notas == 0.10):
            print("{} moedas(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 0.05
            Tonotas = 0
        elif(Notas == 0.05):
            print("{} moedas(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 0.01
            Tonotas = 0
        elif(Notas == 0.01):
            print("{} moedas(s) de R$ {:.2f}".format(Tonotas, Notas))
            Notas = 0.0
        if(Total == 0):
            break
