ld = []#deixaram fila
np = int(input())#numero de pessoas
if(np >= 1 and np <= 50000):
    nn = input().split()#numeros inteiros
    m = int(input())#quantidade de pessoas que deixaram a fila
    mp = input().split()#identificadores das pessoas que deixaram fila
    for i in mp:
        i1 = nn.index(i)
        nn.pop(i1)
    sem_lista = " ".join(nn)
    print(sem_lista)
