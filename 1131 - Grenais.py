In = 0; Gr = 0;Emp = 0; Gren = 0
while True:
    Int, Gre = str(input()).split()
    Int = int(Int); Gre = int(Gre)
    if(Int > Gre):
        In += 1
    elif(Gre > Int):
        Gr += 1
    elif(Int == Gre):
        Emp += 1
    Gren += 1
    N = int(input("Novo grenal (1-sim 2-nao)\n"))
    if(N == 2):
        break
print("{} grenais".format(Gren))
print("Inter:{}".format(In))
print("Gremio:{}".format(Gr))
print("Empates:{}".format(Emp))
if(In > Gr):
    print("Inter venceu mais")
elif(Gr > In):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
