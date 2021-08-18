total_idade =0
maisvelho=0
cont = 0
for pessoas in range (0,4):
    nome = (input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = (input('m ou f: '))
    total_idade=total_idade+idade
    if idade > maisvelho:
        maisvelho = idade
        nome_mais_velho = nome
    if idade < 20 and sexo =='f':
        cont=cont+1

print('MEDIA DAS IDADES: {}'.format(total_idade/4))
print('NOME DO MAIS VELHO: {}'.format(nome_mais_velho))
print('Mulheres com mais de 20 nos: {}'.format(cont))
