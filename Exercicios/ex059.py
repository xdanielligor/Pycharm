from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DA PÁGINA''')
    opcao = int(input('Qual a opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} X {n2} é {produto}')
    elif opcao == 3:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print(f'O maior número é o {maior}')
    elif opcao == 4:
        print('Você escolheu \033[31mNovos Números!\033[m Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        print('==='*10)
        sleep(2)
print('Fim do programa! Volte sempre!')
