cont =0
cont_total=0
op='s'
n=0
maior=0
menor=0
while op != 'N':
    
    n=int(input('Numero: '))
    cont +=1
    cont_total = cont_total+n
    op = input('Quer digitar outro numero? [n\s]').upper()
    if cont ==1:
        maior = menor = n
    if n >maior:
        maior= n
    if n < menor:
        menor = n
print('MAIOR: {} \nMENOR {}'.format(maior,menor))
print('A média é: {}'.format(cont_total/cont))