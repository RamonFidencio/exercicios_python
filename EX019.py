import random
import math
nomes =[]
nome='fa'
i=0
while (nome!='0'):
    nome = str (input("Digite o nome do aluno: (Digite-0 para sortear)" ))
    nomes.append(nome)
    i = i+1
else:
    i=i-1
    escolhido = int (random.uniform(0,i))
    print ('O Aluno escolhido foi: {}'.format(nomes[escolhido]))
    