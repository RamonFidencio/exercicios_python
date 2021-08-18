lista = []
while True:
    n = int(input('\n\nNUMERO: '))
    res=str(input('Deseja digitar um novo numero [S/N]: ').upper())
    lista.append(n)
    if res == 'N':
        break
print(f'Foran digitados: {len(lista)} numeros')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado') 