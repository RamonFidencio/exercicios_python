lista = []
c=0
while True:
    n = int(input('\n\nNUMERO: '))
    res=str(input('Deseja digitar um novo numero [S/N]: ').upper())
    if n not in lista:
        lista.append(n)
    else:
        print('Repetido e nã ofoi adicionado...')
    if res == 'N':
        break
lista.sort()
print(lista)