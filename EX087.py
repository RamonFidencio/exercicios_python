matriz=[[0,0,0],[0,0,0],[0,0,0]]
som=0
som3=0
maior=0
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c]=(int(input('Numero: ')))
        som=som+matriz[l][c]
        if c==2:
            som3=som3+matriz[l][c]
        if l ==1:
            if matriz[l][c]>maior:
                maior=matriz[l][c]

for l in range (0,3):
    for c in range(0,3):  
        print(f'[{matriz[l][c]}]',end='')
    print()

print(f'Somatorio: {som}')
print(f'Somatorio 3 coluna: {som3}')
print(f'Mair da 2 linha: {maior}')