n = int(input('Digite um némero inteiro: '))
print("""Escolha uma das opçãoes abaixo:
[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexagonal""")
op = int (input('Sua opção: '))
if op == 1 :
    print(f'{n} Convertido para binario é igual a {bin(n)[2:]}')
elif op == 2:
    print(f'{n} Convertido para Octal é igual a {oct(n)[2:]}')
elif op == 3:
    print(f'{n} Convertido para Hexagonal é igual a {hex(n)[2:]}')
else:
    print('Opção invalida, Tente novamente!')