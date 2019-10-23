N = int(input())
total = 0; tc = 0; ts = 0; tr = 0
for c in range(N):
    q, t = str(input()).split()
    t = str(t)
    q = int(q)
    # Analisando Coelhos
    if(t == "C"):
        total = total + q
        tc += q
    # Analisando Ratos
    if(t == "R"):
        total += q
        tr += q
    # Analisando Sapos
    if(t == "S"):
        total += q
        ts += q
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(tc))
print("Total de ratos: {}".format(tr))
print("Total de sapos: {}".format(ts))
print("Percentual de coelhos: {:.2f} %".format((100 * tc)/total))
print("Percentual de ratos: {:.2f} %".format((100 * tr)/total))
print("Percentual de sapos: {:.2f} %".format((100 * ts)/total))
