d = float(input('Qual a distancia da sua viagem: '))
print(f'Você está prestes a começar uma viagem de {d}KM')
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print(f'O preço da sua passagem será de R${preco:.2f}')