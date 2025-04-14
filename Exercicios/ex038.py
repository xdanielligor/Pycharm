a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('O \033[35mPRIMEIRO\033[m valor é maior.')
elif b > a:
    print('O \033[32mSEGUNDO\033[m valor é maior.')
else:
    print('Os valores são \033[37mIGUAIS')