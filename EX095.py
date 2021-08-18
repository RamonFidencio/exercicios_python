jogadores=list()
jogador={}
gols=list()
while True:
    soma_gols=0
    jogador['nome']=str(input('Nome: '))
    jogador['jogos']=int(input('Numero de jogos: '))
    
    for n in range (0,jogador['jogos']):
        gols.append(int(input(f'Quantos gols ele fez no jogo{n+1}: ')))
        soma_gols=soma_gols+gols[n]
    
    jogador['gols']=gols[:]
    print(jogador['gols'])
    jogador['soma_gols']=soma_gols
    
    gols.clear()
    jogadores.append(jogador.copy())
    resp=input('Deseja cadastrar um novo jogador? [S/N]' ).upper()
    if resp =='N':
        break
print('-='*30)
for i,v in enumerate(jogadores):
    print(f'{i}{v["nome"]:>10}{v["soma_gols"]:>10}')
print('-='*30)

while True:
    indice=int(input('Deseja saber o aproveitamento de qual jogador? '))
    print(f'--LEVANTAMENTO DO JOGADOR {jogadores[indice]["nome"]}--')
    for i,v in enumerate(jogadores[indice]['gols']) :
        print(f'No jogo {i} fez {v} gols!')
    if indice == 999:
        break
