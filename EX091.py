from random import randint
from pprint import pprint
jogadores=list()
for n in range (1,5):
    jogada={'Nome':n,'dado':randint(1,6)}
    jogadores.append(jogada)
    print(f'O jogador {jogada["Nome"]} tirou o numero: {jogada["dado"]}')
rank=sorted(jogadores,key=lambda k: k['dado'])
print(rank)

