v = int(input())
ano = (v -(v % 365)) / 365
mes = ((v % 365) - ((v % 365)%30)) / 30
dia = (v % 365) % 30
print("{:.0f} ano(s)".format(ano))
print("{:.0f} mes(es)".format(mes))
print("{:.0f} dia(s)".format(dia))
