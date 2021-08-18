preco= float (input ("Preço: "))
pag = int(input('Pagemnto: \n1 - A vista (10%' 'de desconto)\n2- Cartão 1x (5%' 'de desconto)\n3- Cartão 2x (Preço normal)\n4- Cartão 3x (20%' 'de Acrescimo)\n'))
if pag == 1:
    print('Você pagará: {}'.format(preco*0.9))
elif pag == 2:
    print('Você pagará: {}'.format(preco*0.95))
elif pag ==3:
    print('Você pagará: {}'.format(preco))
elif pag ==4:
    print('Você pagará: {}'.format(preco*1.2))
