p_maiores=0
n_homens=0
m_menores=0
res='S'
while res == 'S':
    i=int(input('IDADE: '))
    s=(input('SEXO: [M/F]')).upper()
    if i >=18:
        p_maiores +=1
    if s == 'M':
        n_homens +=1
    if s == 'F' and i<20:
        m_menores +=1
    res=input('QUER CADASTRAR UMA NOVA PESSOA? [S/N]: ').upper()
print('-'*30,f'\n\nPESSOAS COM MAIS DE 18: {p_maiores}')
print(f'NUMERO DE HOMES CADASTRADOS: {n_homens}')
print(f'MULHERES COM MENOS DE 20 ANOS: {m_menores}')