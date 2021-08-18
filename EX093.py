jogador={}
gols=[]
soma_gols=0
jogador['nome']=str(input('Nome: '))
jogador['jogos']=int(input('Numero de jogos: '))
for n in range (0,jogador['jogos']):
    gols.append(int(input(f'Quantos gols ele fez no jogo{n+1}: ')))
    soma_gols=soma_gols+gols[n]
jogador['gols']=gols
jogador['soma_gols']=soma_gols
print (jogador)
print('-='*30)
for v,k in jogador.items():
    print(f'O campo {v} tem o valor {k}')
print('-='*30)
print(f'O jogador {jogador["nome"]}, jogou {jogador["jogos"]} Partidas')
for i,v in  enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {v} gols!')
