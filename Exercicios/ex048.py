soma = 0
count = 0

for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        count+= 1
print(f'A soma de todos os {count} valores solicitador é {soma}')