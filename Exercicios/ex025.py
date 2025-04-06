frase = str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece {frase.count('A')} na frase!')
print(f'A letra A aparece na posição {frase.find('A') + 1}')
print(f'A ultima letra aparece na {frase.rfind('A') + 1} posição')