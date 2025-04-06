n = int(input('Informe um número: '))
u = n//1%10
d = n //1%100
c = n // 1%1000
m = n // 1%10000
print(f'Analizando o número {n}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')