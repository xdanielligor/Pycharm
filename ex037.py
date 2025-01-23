nome = str(input('Qual seu nome: '))
if nome == 'Daniel':
    print(f'Que nome feio você tem {nome}!')
elif nome == 'José' or nome == 'Maria':
    print('Seu nome é muito comum no Brasil!')
elif nome in 'Ana Fernanda Claudia Juliana':
    print('Belo nome feminino!')
else:
    print('Você tem um nome comum')