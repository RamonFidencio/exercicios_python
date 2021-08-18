alunos=list()
while True:
    nome=(input('Nome: '))
    nota1=(float(input('Nota 1: ')))
    nota2=(float(input('Nota 2: ')))
    media=(nota1+nota2)/2
    alunos.append([nome,[nota1,nota2],media])
    cond=input('Deseja cadastrar um novo aluno? [S/N]').upper()
    if cond =='N':
        break
print(f'-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print(f'-='*26)
for i,a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc=int(input('Mostra notas de qual aluno? (999-para)'))
    if opc==999:
        break
    if opc <= len(alunos)-1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')

