count = total = 0
print('''[ 1 ] CAIXA
[ 2 ] MARCAR
[ 3 ] SAIR''')
opcao = int(input('Opção desejada: '))

if opcao == 1:
    while True:
        q = int(input('Quantas pipocas: '))
        if q == 999:
            break
        count += q
        total = count * 8
if opcao == 2:
    nome = str(input('Nome da pessoa: '))
if opcao == 3:
    print('Finalizando')

print(f'O quantidade vendida foi R${total} e o total {count}')
