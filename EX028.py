import random
n = int (input ("Escolha um numeor entre 1-5: "))
number = random.randint(1,5)
if (n==number) :
    print("Você acertou {} = {}".format(n,number))
else:
    print("Você errou {} != {}".format(n,number))