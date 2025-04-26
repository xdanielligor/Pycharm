import random
print('''Que tipo de exercicio você quer 
[ 1 ] \033[31mTipos Primitivos\033[m
[ 2 ] \033[32mOperadores Aritmeticos\033[m
[ 3 ] \033[33mModulos\033[m
[ 4 ] \033[34mManipulação de texto\033[m
[ 5 ] \033[35mCondições\033[m
[ 6 ] \033[36mRepetição For\033[m
[ 7 ] \033[37mRepetição While\033[m''')
n = int(input('Escolha: '))
if n == 1:
    num = random.randint(1,4)
    print(f'O exercicio sorteado foi {num}')
elif n == 2:
    num = random.randint(5, 15)
    print(f'O exercicio sorteado foi {num}')
elif n == 3:
    num = random.randint(16, 21)
    print(f'O exercicio sorteado foi {num}')
elif n == 4:
    num = random.randint(22, 27)
    print(f'O exercicio sorteado foi {num}')
elif n == 5:
    num = random.randint(28, 45)
    print(f'O exercicio sorteado foi {num}')
elif n == 6:
    num = random.randint(46, 56)
    print(f'O exercicio sorteado foi {num}')
elif n == 7:
    num = random.randint(57, 65)
    print(f'O exercicio sorteado foi {num}')
else:
    print('Opção Invalida!')