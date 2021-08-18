from random import randint
def sorteio(lista):
    for i in range(0,5):
        lista.append(randint(0,10))
    return lista

def somaPar(lista):
    soma=0
    for i in lista:
       if i%2==0:
           soma+=i
    return print(soma)

lista=[]
sorteio(lista)
print(lista)
somaPar(lista)
