def ficha(nome='<DESCONHECIDO>',gols=0):
    return print(f'O jogador {nome} fez {gols} gols!')

n=input('Qual o nome do jogador: ')
g=(input('Quantos gols ele fez: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gols=g)
else:
    ficha(n,g)
