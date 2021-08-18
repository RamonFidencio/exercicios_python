lista=list()
pessoa={}
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('NOME: '))
    pessoa['sexo']=str(input('SEXO [M/F]:')).upper()
    pessoa['idade']=int(input('Idade: '))
    lista.append(pessoa.copy())
    soma+=pessoa['idade']
    resp=input('Deseja cadastrar uma nova pessoa? [S/N]').upper()
    if resp=='N':
        break
print(f'Foram cadastradas {len(lista)}')
print(f'A média de idades é: {soma/len(lista)}')
print('Mulheres:')
for p in lista:
    if p['sexo']=='F':
        print(p['nome'])
print('pessoas maiores de idade:')
for p in lista:
    if p['idade']>=18:
        print(p['nome'])