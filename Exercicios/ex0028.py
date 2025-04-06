velocidade = float(input('Velocidade atual: '))
if velocidade > 80:
    print(f'Multado!!! Você exedeu o limite permitido que é 80km/h você deve pagar a multa de R${(velocidade - 80) * 7}')
print('Tenha um bom dia! Dirija com segurança!')