n1 = int (input ("1° Numero: "))
n2 = int (input ("2° Numero: "))
n3 = int (input ("3° Numero: "))
if((n1+n2)>n3) and ((n2+n3)>n1) and ((n1+n3)>n2):
    print('POSSIVEL')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('IMPOSSIVEL')
