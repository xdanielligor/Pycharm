from tensorflow.python.tpu.tensor_tracer_report import proto_fingerprint

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma /quant
print(f'Você digitou {quant} números e a media foi {media}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')