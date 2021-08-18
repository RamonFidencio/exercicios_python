lista = []
maior=0
i_maior=0
menor=0
i_menor=0
for n in range (0,5):
    lista.append(int(input('NUMERO: ')))
    if n ==0:
        menor=lista[n]
    else:
        if lista[n]>maior:
            maior=lista[n]
        if lista[n]<menor:
            menor=lista[n]
print(f'O maior numero digitado foi: {maior} nas posições ',end='')
for i ,v in enumerate(lista):
    if lista[i]==maior:
        print(f'{i}...',end='')
print(f'O menor numero digitado foi: {menor} nas posições ',end='')
for i ,v in enumerate(lista):
    if lista[i]==menor:
        print(f'{i}...',end='')