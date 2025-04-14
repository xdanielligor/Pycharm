import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18,
         19, 20, 21, 22, 23, 24, 25]

n = random.choice(lista)
print(f"Exercício de número {n}, Boa sorte!")
if n == 18:
    print("""Digite o angulo que você deseja: 30
    O angulo de 30.0 tem o seno de 0.50
    O angulo de 30.0 tem o consseno de 0.87
    O angulo de 30.0 tem o tangente de 0.58""")
elif n == 4:
    print("""Digite algo: Programador
    O tipo primitivo desse valor é <class 'str'>
    Só tem espaços: false
    É um número: False
    É um alfabetico: True
    É um alfanúmerico: True
    Está em MAIUSCULA: false
    Está em ninuscula: false
    Está capitalizada: true""")
elif n == 24:
    print("""Em que cidade você nasceu? SAnto Inacio
    True""")

else:
    print(f"O número sorteado foi {n} Boa sorte!")