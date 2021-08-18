temp=[]
pessoas=[]
lista_pesados=[]
maior_peso=0
menor_peso=0
lista_leves=[]
while True:
    temp.append(input('\n\nNOME: '))
    temp.append(float(input('PESO: ')))
    res=str(input('Deseja digitar um novo numero [S/N]: ').upper())
    pessoas.append(temp[:])
    
    if temp[1] > maior_peso:
        maior_peso=temp[1]

    if len(pessoas)==1:
        menor_peso=temp[1]
    elif temp[1]<menor_peso:
        menor_peso=temp[1]

    temp.clear()
    if res == 'N':
        break
for p in pessoas:
    if p[1]==maior_peso:
        lista_pesados.append(p[0])
    if p[1]==menor_peso:
        lista_leves.append(p[0])

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso é {maior_peso}. Peso de {lista_pesados}')
print(f'O menor peso é {menor_peso}. Peso de {lista_leves}')