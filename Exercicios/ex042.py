s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3< s1 + s2:
    print('Os segmentos podem formar um triangulo ', end ='')
    if s1 == s2 == s3:
        print(' EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCÁLENO!')
    else:
        print('ESÓSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR UM TRIANGULO!')