t = int(input('Numero: '))
r = int(input('Razão: '))
dez = t + (10-1)*r
for t in range (t,dez+r,r):
    print(t)