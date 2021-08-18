cont1 =0
cont2 =0 
maior_peso=0
menor_peso = 5000

for pesos in range (0,5):
    peso = float(input('Peso: '))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso= peso

print('O MAIOR PESO: {}'.format(maior_peso))
print('O MENOR PEOS: {}'.format(menor_peso))

