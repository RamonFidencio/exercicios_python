n = int (input ("Numero: "))
escolha = 4
while(escolha != 0):
    escolha = int (input ("\n1- base2\n2- base8\n3- base16\nOpção: "))
    if escolha == 1:
        print('\n {}'.format(bin(n)))
    elif escolha == 2:
        print('\n {}'.format(oct(n)))
    elif escolha == 3:
        print('\n {}'.format(hex(n)))
    elif (escolha != 0):
        print("opção inválida")