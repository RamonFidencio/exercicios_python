number = int(input ('Enter a number between 0 and 9999: '))
print (f'\nMilhar:  {number//1000%10}\nCentena: {number//100%10}\nDezena: {number//10%10}\nUnidade: {number//1%10}',)
