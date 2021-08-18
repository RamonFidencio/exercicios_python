lista = []
anterio=0
sucessor=0
for c in range (0,5):
    n = int(input('NUMERO: '))
    if c==0:
        sucessor=n
        lista.append(n)
    if c==1 and n>lista[0]:
        lista.append(n)
    elif c==1 :
        lista.insert(0,n)
        print(lista)
    if c>1:
        for i,v in enumerate(lista):
                if n < lista[i]:
                    lista.insert(i,n)
                    print(lista)
                    break

