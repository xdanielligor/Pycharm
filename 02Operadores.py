import math

n = [1, 2, 3, 4, 5, 6, 7, 8]

print("""
Selecione as opções:
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão (Float)
[ 5 ] Divisão inteira
[ 6 ] Módulo
[ 7 ] Potência
[ 8 ] Raiz quadrada
""")

opcao = int(input("Digite a opção desejada: "))

if opcao in [1, 2, 3, 4, 5, 6, 7]:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    if opcao == 1:
        print("Soma:", a + b)
    elif opcao == 2:
        print("Subtração:", a - b)
    elif opcao == 3:
        print("Multiplicação:", a * b)
    elif opcao == 4:
        print("Divisão (float):", a / b if b != 0 else "Não é possível dividir por zero")
    elif opcao == 5:
        print("Divisão inteira:", a // b if b != 0 else "Não é possível dividir por zero")
    elif opcao == 6:
        print("Módulo:", a % b if b != 0 else "Não é possível dividir por zero")
    elif opcao == 7:
        print("Potência:", a ** b)

    # Exemplo sem quebra de linha
    print(f'A soma dos valores é {a + b}', end=" ")
    print(f'A subtração dos valores é {a - b}')

elif opcao == 8:
    num = float(input("Digite um número para calcular a raiz quadrada: "))
    if num >= 0:
        raiz = math.sqrt(num)
        print(f"Raiz quadrada de {num} é {raiz:.2f}")
    else:
        print("Não é possível calcular raiz quadrada de número negativo.")
else:
    print("Opção inválida!")
