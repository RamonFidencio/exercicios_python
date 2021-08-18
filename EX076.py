itens=('abacate',2.75,'Laranja',0.69,'Melancia',1.79,'Banana', 2.89,'Bergamota',8.96)

print('-'*40)
print(' '*10,'LISTAGEM DE PREÇOS')
print('-'*40)
for c in range (0,9):
    if c%2==0 or c== 0:
        n=30-len(itens[c])
        print(f'{itens[c]}','.'*n,f'R${itens[c+1]}')
print('-'*40)