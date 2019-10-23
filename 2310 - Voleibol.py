n = int(input())
ps = 0;pb = 0;pa = 0
ps1 = 0;pb1 = 0;pa1 = 0
for i in range(n):
    nj = input()
    s, b, a = input().split()
    s1, b1, a1 = input().split()
    s = int(s);b = int(b);a = int(a)
    s1 = int(s1);b1 = int(b1);a1 = int(a1)
    ps += s;pb += b;pa += a# somas totais
    ps1 += s1;pb1 += b1;pa1 += a1# Somas sucessos
# calculos
psaques = (ps1 * 100)/ps #porcentagem
pbloqueio = (pb1 * 100)/pb #porcentagem
pataque = (pa1 * 100)/pa #porcentagem
print("Pontos de Saque: {:.2f} %.".format(psaques))
print("Pontos de Bloqueio: {:.2f} %.".format(pbloqueio))
print("Pontos de Ataque: {:.2f} %.".format(pataque))
