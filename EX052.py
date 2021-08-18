cont=0
n = int(input('Numero: '))
for c in range (1,n):
    if(n%c==0):
        cont=cont+1
if cont == 1:
    print('PRIMO')
else:
    print('NÃO É PRIMO')
  
