cont =0
cont_total=0
n=0
while n != 999:
    n=int(input('Numero: '))
    if (n!=999):
        cont +=1
        cont_total = cont_total+n
print('Digitou {} numeros!'.format(cont))
print('Somatorio é: {}'.format(cont_total))