from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade}')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')


