frase= str(input('Frase: ')).strip().upper()
separada = frase.split()
junta = ''.join(separada)
inverso = ''
for letra in range (len(junta)-1,-1,-1):
    inverso += junta[letra]
if inverso == junta:
    print('É UM PALINDROMO')
else:
    print('NÃO É UM PALINDROMO')

