numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    n = int(input('Digite um numero: [0-10]: '))
    if n < 0 or n>10:
        print('INVALIDO !!!')
        break
    else:
        print(f'Voce digitou {numeros[n]}')

