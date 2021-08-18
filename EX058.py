import random
cont = 1
n = int (input ("Escolha um numeor entre 1-10: "))
number = random.randint(0,10)
while n != number:
    n = int (input ("\nVOCÊ ERROU! \n\nEscolha um numeor entre 1-10: "))
    cont=cont+1
print('PARABENS VOCÊ ACEROTU !!  Precisou apens de {} tentaivas.'.format(cont)) 