lista = []
impares = []
pares = []
while True:
    n = int(input('NUMERO: '))
    lista.append(n)
    res=str(input('Deseja digitar um novo numero [S/N]: ').upper())
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
    if res == 'N':
        break

print(lista)
print(pares)
print(impares)