n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = ( n1 + n2 )/ 2
if 7 < media > 5:
    print('O aluno está de RECUPERAÇÃO!!')
elif media < 5:
    print('O aluno está REPROVADO!')
else:
    print('O aluno está APROVADO!')