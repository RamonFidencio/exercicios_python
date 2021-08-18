num=(int(input('Digite um numero; ')),int(input('Digite um numero; ')),int(input('Digite um numero; ')),int(input('Digite um numero; ')))
cont9=0
print('\n\nNumeros pares: ')
for c in range (0,4):
    if num[c]==9:
        cont9+=1
    if num[c]%2==0:
        print(f'{num[c]}')
print(f'Primeira ocorrencia do 3: {num.index(3)+1} posição.')
print(f'O valor 9 apareceu {cont9} vezes')
