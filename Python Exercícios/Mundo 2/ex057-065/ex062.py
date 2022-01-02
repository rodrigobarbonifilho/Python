print('Gerador de PA')
print(10*'-=')
pt = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
qntt = 0
tm = 10
while qntt < tm:
    print(f'{pt} → ', end='')
    pt += r
    qntt += 1
    if qntt == tm:
        print('PAUSA')
        tm += int(input('\nQuer mostrar mais alguns termos? Quantos termo? '))
print(f'O programa foi finalizado com {tm} termos mostrados!')
