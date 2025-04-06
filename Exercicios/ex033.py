sf = float(input('Qual o salario do funcionario:R$ '))
if sf <= 1250:
    novo = sf + (sf*15/100)
else:
    novo = sf + (sf*10/500)
print(f'Quem ganhava R${sf} passa a ganhar R${novo}')