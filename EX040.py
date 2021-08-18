n1 = int (input ("NOTA 1: "))
n2 = int (input ("NOTA 2: "))
nota= (n1+n2)/2
if (nota) < 5 :
    print('REPROVADO')
elif nota >= 5 and nota < 7 :
    print('RECUPERAÇÃO')
elif(nota) >= 7 :
    print('APROVADO')