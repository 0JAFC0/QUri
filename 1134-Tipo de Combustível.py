#1. Álcool 2.Gasolina 3.Diesel 4.Fim
A = 0; G = 0; D = 0; N = 0
while(N != 4):
    N = int(input())
    if(N == 1):
        A += 1
    elif(N == 2):
        G += 1
    elif(N == 3):
         D += 1
print("MUITO OBRIGADO")
print("Alcool: {}".format(A))
print("Gasolina: {}".format(G))
print("Diesel: {}".format(D))
