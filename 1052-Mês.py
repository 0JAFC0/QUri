Mes = int(input())
Lmes = ["January","February","March","April","May","June","July","August","September","October","November","December"]
p = 0
nelementos = len(Lmes)
Mes = Mes - 1# Subtrai da Variavel Para quê ela seja igual ao Numero de Itens da Lista
while(p <= nelementos):
    if(p == Mes):
        print(Lmes[p])
        
    p += 1
