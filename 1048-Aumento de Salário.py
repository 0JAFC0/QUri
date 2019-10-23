"""Dante

sal = float(input())
sal = ("{:.2f}".format(sal))
sal = float(sal)
p = [0.15,0.12,0.10,0.07,0.04]
val = [0,400.00,800.00,1200.00,2000.00,0]
c = 0
while c < 5:
    if (sal > (val[c])) and (sal <= (val[c+1])):
        reaj = sal * p[c]
        tot = sal + reaj
        per = p[c]*100
    elif (sal > 2000.00):
        reaj = sal*0.04
        tot = sal + reaj
        per = 4
    c += 1
print("Novo salario: {:.2f}".format(tot))
print("Reajuste ganho: {:.2f}".format(reaj))
print("Em percentual: {:.0f}".format(per))
"""

"""Arthur"""

salario = float(input())

if(salario >= 0 and salario <= 400.00):
    reajuste = (salario*0.15)+salario
    ganho = reajuste - salario
    percentual = 15
else:
    if(salario > 400.01 and salario <= 800.00):
        reajuste = (salario*0.12)+salario
        ganho = reajuste-salario
        percentual = 12
    else:
        if(salario >= 800.01 and salario <= 1200.00):
            reajuste = (salario*0.10)+salario
            ganho = reajuste-salario
            percentual = 10
        else:
            if(salario >= 1200.01 and salario <= 2000.00):
                reajuste = (salario*0.07)+salario
                ganho = reajuste - salario
                percentual = 7
            else:
                if(salario >= 2000.01):
                    reajuste = (salario*0.04)+salario
                    ganho = reajuste-salario
                    percentual = 4
print("Novo salario: {:.2f}".format(reajuste))
print("Reajuste ganho: {:.2f}".format(ganho))
print("Em percentual: {} %".format(percentual))
