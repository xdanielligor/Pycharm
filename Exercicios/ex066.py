count = s = n = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    count += 1
    s += n
print(f'a soma dos {count} valores foi {s}! ')