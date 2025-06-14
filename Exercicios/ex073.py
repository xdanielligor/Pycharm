times =  ('Corinthians', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
               'São Paulo', 'Botafogo', 'Bahia', 'Cruzeiro', 'Vasco da Gama',
               'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino',
               'Atlético-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print('-='*15)
print(f'Lista de times do brasileirão {times}')
print('-='*15)
print(f'Os cinco primeiros times são {times[0:5]}')
print('-='*15)
print(f'Os quatro últimos são {times[-4:]}')
print('-='*15)
print(f'Times em oredem alfabetica: {sorted(times)}')
print('-='*15)
print(f'A posição do Vasco da Gama é {times.index("Vasco da Gama")+1}° posição')