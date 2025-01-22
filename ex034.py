print('=' * 30)
print('Anlizador de triangulos')
print('=' * 30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a +c and c < a + b:
    print('Os seguimentos \033[31mPODEM\033[m formar um triangulo')
else:
    print('Os segmentos NÃO PODEM formar um triangulo')