print(14*'-=')
print(f'{"BANCO CEV":^28}')
print(14*'-=')
saque = int(input('Quanto voce quer sacar? '))
print(14*'==')
while True:
    nota50 = (saque // 50)
    saque -= nota50 * 50
    nota20 = saque // 20
    saque -= nota20 * 20
    nota10 = saque // 10
    saque -= nota10 * 10
    nota1 = saque // 1
    saque -= nota1 * 1
    if saque == 0:
        break
print(f'No total deu {nota50} notas de R$50,00' if nota50 > 0 else '', end='')
print(f'\nNo total deu {nota20} notas de R$20,00' if nota20 > 0 else '', end='')
print(f'\nNo total deu {nota10} notas de R$10,00' if nota10 > 0 else '', end='')
print(f'\nNo total deu {nota1} notas de R$1,00' if nota1 > 0 else '')
print(14*'==')
print('VOLTE SEMPRE AO BANCO CEV!')
