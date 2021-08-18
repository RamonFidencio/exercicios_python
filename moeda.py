def metade(valor):
    return print(f'A metade de R${valor} é R${valor/2}')
def dobro(valor):
    return print(f'O dobro de R${valor} é R${valor*2}')
def aumentar(valor,mult):
    return print(f'R${valor} acrescido de {mult}% é R${(valor*(1+mult*(0.01))):1f}')
def diminuir(valor,mult):
    return print(f'R${valor}diminuido de {mult}% é R${valor*(100-mult)*0.01}')
