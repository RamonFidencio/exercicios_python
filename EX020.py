import random
import math
nomes =[]
nome='fa'
i=0
while (nome!='0'):
    i = i+1
    nome = str (input("Digite o nome do aluno: (Digite-0 para sortear)" ))
    nomes.append(nome)
    
else:
    nomes.remove('0')
    escolhido = int (random.uniform(0,i))
    random.shuffle(nomes)
    print ('A orden de apresentação: {}'.format(nomes))
    