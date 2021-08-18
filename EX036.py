valorcasa = int (input ("Valor da casa: "))
salario = int (input ("Salário: "))
tempo = int (input ("Quantos anos vai pagar: "))*12
valormes = valorcasa/tempo
if(valormes>(salario*0.3)):
    print('NÃO É POSSIVEL COMPRAR')
else:
    print('É POSSIVEL COMPRAR ')