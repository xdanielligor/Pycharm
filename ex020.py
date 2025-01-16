import random
from random import shuffle
p = str(input('Primeiro nome: '))
s = str(input('Segundo nome: '))
t = str(input('Terceiro nome: '))
lista = [p,s,t]
random.shuffle(lista)
print(f'A ordem sera {lista}')