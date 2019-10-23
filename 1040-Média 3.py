N1 , N2, N3, N4 = str(input()).split()
N1 = float(N1); N2 = float(N2); N3 = float(N3); N4 = float(N4)
Mediap = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/(2+3+4+1)
print("Media: {:.1f}".format(Mediap))
if(Mediap >= 7.0):
    print("Aluno aprovado.")
elif(Mediap < 5.0):
    print("Aluno reprovado.")
elif(Mediap >= 5.0 and Mediap <= 6.9):
    print("Aluno em exame.")
    Nexame = float(input())
    print("Nota do exame: {:.1f}".format(Nexame))
    Nmedia = (Mediap + Nexame) / 2
    if(Nmedia >= 5.0 and Nmedia <= 10.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(Nmedia))

