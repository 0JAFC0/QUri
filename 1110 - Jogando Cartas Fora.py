
n = int(input())
while(n != 0):
    pilha = []
    dcard = []

    for c in range(n, 0, -1):
        pilha.append(c)

    while(len(pilha) >= 2):
        dcard.append(str(pilha.pop()))
        pilha.insert(0, str(pilha.pop()))
    if(len(dcard) == 0):
        print("Discarded cards:")
    else:
        print("Discarded cards:", ", ".join(dcard))
    
##    for d in range(len(dcard)):
##        if(dcard[d] == dcard[len(dcard)-1]):
##            print("{}".format(dcard[d]), end="")
##        else:
##            print("{}".format(dcard[d]), end=", ")

    print("Remaining card: {}".format(pilha[0]))
    n = int(input())
