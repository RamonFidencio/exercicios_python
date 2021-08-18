total=0
caros=0
mais_barato='barato'
menor_preco=100000
while True:
    preco=int(input('PREÇO DO PRODUTO: '))
    nome=(input('NOME DO PRODUTO: ')).upper()
    total +=preco
    if preco > 1000 :
        caros+=1
    if preco < menor_preco:
        mais_barato = nome
        menor_preco = preco
    res=input('QUER CADASTRAR UMA NOVO PRODUTO? [S/N]: ').upper()
    if res == 'N':
        break
print('-'*30,f'\n\nTOTAL GASTO: {total}')
print(f'PRODUTOS QUE CUSTAM MAIS DE r$1000: {caros}')
print(f'PRODUTO MAIS BARATO: {mais_barato}')