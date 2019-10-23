A1 = int(input())
A2 = int(input())
A3 = int(input())
Primeiro = (A2*2)+(A3*4)
Segundo = (A1+A3)*2
Terceiro = (A1*4)+(A2*2)
if(Primeiro <= Segundo and Primeiro <= Terceiro):
    r = (A2*2)+(A3*4)
else:
    if(Segundo <= Primeiro and Segundo <= Terceiro):
        r = (A1+A3)*2
    else:
        if(Terceiro <= Primeiro  and Terceiro <= Segundo):
            r = (A1*4)+(A2*2)
print(r)
