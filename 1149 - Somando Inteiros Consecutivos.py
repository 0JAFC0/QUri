x = str(input()).split()
a = int(x[0])
n = int(x[len(x)-1])
soma = 0
while(n == 0):
  n = input()
  n = int(n)
for i in range(n):
  soma += (a + i)
print(soma)
