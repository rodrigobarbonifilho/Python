print('Gerador de PA')
print(10*'-=')
pt = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
tm = 0
while tm < 10:
    print(f'{pt} → ', end='')
    pt += r
    tm += 1
print('FIM')
