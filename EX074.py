from random import randint
maior=0
menor=11
numeros=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for c in range(0,5):
    print(f'{numeros[c]}',end=' -> ')
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f'\n\nMaior: {maior}')
print(f'Menor: {menor}')