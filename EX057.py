sexo= str(input('SEXO: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('DIGITE UM VALOR CORRETO !!! SEXO: ')).strip().upper()[0]
print('Dados registrados !')
