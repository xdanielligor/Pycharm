sexo = str(input('Informe o sexo: [M / F] ')).strip().upper()[0]
while sexo not in 'M F':
    sexo = str(input('Dados \033[31mInvalidos\033[m')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
