N = float(input())
N += 0.001
if (0 <= N and N <= 1000000.00):
    n100 = N//100
    r100 = N%100
    n50 = r100//50
    r50 = r100%50
    n20 = r50//20
    r20 = r50%20
    n10 = r20//10
    r10 = r20%10
    n5 = r10//5
    r5 = r10%5
    n2 = r5//2
    r2 = r5%2
    n1 = r2//1
    r1 = r2%1
    n050 = r1//0.50
    r050 = r1%0.50
    n025 = r050//0.25
    r025 = r050%0.25
    n010 = r025//0.10
    r010 = r025%0.10
    n005 = r010//0.05
    r005 = r010%0.05
    n001 = r005//0.01
    r001 = r005%0.01
    print("NOTAS:")
    print("{:.0f} nota(s) de R$ 100.00".format(n100))
    print("{:.0f} nota(s) de R$ 50.00".format(n50))
    print("{:.0f} nota(s) de R$ 20.00".format(n20))
    print("{:.0f} nota(s) de R$ 10.00".format(n10))
    print("{:.0f} nota(s) de R$ 5.00".format(n5))
    print("{:.0f} nota(s) de R$ 2.00".format(n2))
    print("MOEDAS:")
    print("{:.0f} moeda(s) de R$ 1.00".format(n1))
    print("{:.0f} moeda(s) de R$ 0.50".format(n050))
    print("{:.0f} moeda(s) de R$ 0.25".format(n025))
    print("{:.0f} moeda(s) de R$ 0.10".format(n010))
    print("{:.0f} moeda(s) de R$ 0.05".format(n005))
    print("{:.0f} moeda(s) de R$ 0.01".format(n001))

