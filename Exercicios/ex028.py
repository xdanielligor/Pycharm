from random import randint
from time import sleep
computador = randint(0,5)
print('=' * 55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=' * 55)
jogador = int(input('Em que número eu estou pensando: '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! eu pensei no número {computador} e não no {jogador}')