import random
from random import choice

p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
lista = [p,s,t,q]
sorteio = random.choice(lista)
print(f'O nome sorteado foi {sorteio}!')