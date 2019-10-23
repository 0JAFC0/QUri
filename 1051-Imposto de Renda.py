salario = float(input())
if(salario >= 0.00 and salario <= 2000):
    print("Isento")
elif(salario >= 2000.01 and salario <= 3000):
    s = salario - 2000.01
    im = (0.08*s)
    print("R$ {:.2f}".format(im))
elif(salario >=3000.01 and salario <= 4500):
    s = salario - 3000.01
    s1 = 0.18 * 1500
    im = 80 + (0.18*s)
    print("R$ {:.2f}".format(im))
elif(salario >= 4500.01):
    s = salario - 4500.01
    s1 = 0.18 * 1500
    im = s1+(80 + (0.28*s))
    print("R$ {:.2f}".format(im))
