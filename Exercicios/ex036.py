valor = float(input('Valor da casa: '))
salario = float(input('Salario do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar a casa de {valor} em {anos} anos')
print(f'A prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Emprestimo pode ser \033[32mCONCEDIDO')
else:
    print('Emprestimo \033[31mNEGADO')
