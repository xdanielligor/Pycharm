from random import randint
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('''Suas opções:
[ 0 ] pedra
[ 1 ] papel 
[ 2 ] tesoura''')
jogador = int(input('Qual a sua jogada: '))
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[35mJOGADA INVALIDA!')
elif computador == 1:
    if jogador ==0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[35mJOGADA INVALIDA!')
elif computador == 2:
    if jogador ==0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[35mJOGADA INVALIDA!')
