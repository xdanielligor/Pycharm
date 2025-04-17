from datetime import date
atual = date.today().year
tot_menor = 0
tot_maior = 0
for c in range (1,5):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu: '))
    idade = atual - ano
    if idade >=21:
        tot_maior += 1
    else:
        tot_menor += 1
print(f'Ao todo tivemors {tot_maior} pessoas maior de idade')
print(f'E tambem tivemos {tot_menor} pessoas menor de idade')