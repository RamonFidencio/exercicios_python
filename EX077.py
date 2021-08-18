palavras=('arara','leao','baleia')
for p in palavras:
    print(f'\nNa palavra {p} temos: ',end=' ')
    for l in p:
        if l in 'aeiou':
            print(f'{l} ',end='')