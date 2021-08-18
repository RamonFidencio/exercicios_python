phrase = (input ('Frase: ')).upper().strip()
print ('A letra A aparece {} vezes'.format(phrase.count('A')))
print ('A aparece pela primeira vez na posição {}'.format(phrase.find('A')+1))
print ('A aparece pela ultima vez na posição {}'.format(phrase.rfind('A')+1))

