primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro,decimo,razao):
    print(c, end='-> ')
print('ACABOU!')

# outra maneira

'''print('==' * 20)
print(' ' * 10,'10 TERMOS DE UMA PA',' '* 10)
print('==' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
progressao = termo
for c in range(10):
    print(progressao, end= ' → ')
    progressao += razao
print('ACABOU!!!')'''