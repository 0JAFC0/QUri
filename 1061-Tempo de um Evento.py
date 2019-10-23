ni = str(input()).split(" ")
xi, yi, zi = str(input()).split(":")
nf = str(input()).split(" ")
xf, yf, zf = str(input()).split(":")
xi = int(xi); yi = int(yi); zi = int(zi);ni = int(ni[1])
xf = int(xf); yf = int(yf); zf = int(zf);nf = int(nf[1])

diai = (yi*60) + (xi*3600) + zi + (ni*86400)# Segundos totais iniciais
diaf = (yf*60) + (xf*3600) + zf + (nf*86400)# Segundos totais finais

segundo = diaf - diai # Segundos totais
# Parte Dos Segundos
dia = 0
hora = 0
minuto = 0
while(segundo >= 86400):
    dia += 1
    segundo -= 86400
while(segundo >= 3600):
    hora += 1
    segundo -= 3600
while(segundo >= 60):
    minuto += 1
    segundo -= 60
print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(minuto))
print("{} segundo(s)".format(segundo))
