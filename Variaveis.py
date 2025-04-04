# Entrada de string
text = str(input('Qual o seu nome: '))  # str
print(f'Prazer em conhecer você, {text}!')

# Entrada de dados
num_int = int(input('\nDigite um valor inteiro: '))  # int
num_dec = float(input('Digite um valor decimal: '))  # float

# Comparação booleana
vl_bool = num_int > num_dec

# Verificação condicional
if vl_bool:
    print(f'O número {num_int} é maior que {num_dec}.')
elif num_int == num_dec:
    print('Ambos os valores são iguais')
else:
    print(f'O número {num_int} é menor que {num_dec}.')

# Mostrando os valores e seus tipos corretamente
print(f'\nValor de número inteiro: {num_int} | Tipo: {type(num_int)}')
print(f'Valor de número decimal: {num_dec} | Tipo: {type(num_dec)}')
print(f'Valor de valor booleano: {vl_bool} | Tipo: {type(vl_bool)}')
print(f'Valor de texto: {text} | Tipo: {type(text)}')

# Operações entre os tipos
soma = num_int + num_dec  # int + float = float
print(f"\nSoma entre inteiro e float: {num_int}  + {num_dec} = {soma}| Tipo: {type(soma)}")


conv_bool = int(vl_bool)  # Convertendo bool (True = 1, False = 0)  para int
print(f'\nConversão de booleano para inteiro: {conv_bool} | Tipo: {type(conv_bool)}\n')

conca = text + " O número é " + str(num_int)  # Convertendo int para str e concatenando
print(f"Concatenando string com número: {conca} | Tipo: {type(conca)}")