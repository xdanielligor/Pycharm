print(f'{'LOJAS GUANARABA':-^40}')
preco = float(input("Preço das compras: "))
print('''Formas de pagamento
[ 1 ] Á vista no dinheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou manis no cartão''')
opcao = int(input('Qual a opção: '))
if opcao == 1:
    total = preco - (preco* 10/100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco *20/100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total/totalparc
    print(f'Sua compra vai ser parcelada em {totalparc}x de {parcela:.2f}')
else:
    total = 0
    print('Opção invalida de pagamento')
print(f'Sua compra de {preco:.2f} vai custar {total:.2f} no final')