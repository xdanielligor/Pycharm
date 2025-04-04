# Entrada de dados
num_int = int(input('Digite um valor inteiro: '))  # int
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

# Entrada de string
text = str(input('Qual o seu nome: '))  # str
print(f'Prazer em conhecer você, {text}!')

# Mostrando os valores e seus tipos corretamente
print(f'Valor de número inteiro: {num_int} | Tipo: {type(num_int)}')
print(f'Valor de número decimal: {num_dec} | Tipo: {type(num_dec)}')
print(f'Valor de valor booleano: {vl_bool} | Tipo: {type(vl_bool)}')
print(f'Valor de texto: {text} | Tipo: {type(text)}')

# Operações entre os tipos
#soma = numero_inteiro + numero_decimal  # int + float = float
#print("\nSoma entre inteiro e float:", soma, " | Tipo:", type(soma))


#conversao_bool = int(valor_booleano)  # Convertendo bool para int (True = 1, False = 0)
#print("Conversão de booleano para inteiro:", conversao_bool, " | Tipo:", type(conversao_bool))

#concatenacao = texto + " O número é " + str(numero_inteiro)  # Convertendo int para str e concatenando
#print("Concatenando string com número:", concatenacao, " | Tipo:", type(concatenacao))
