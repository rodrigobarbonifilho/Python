pn = 0
sn = 1
tm = 2
print(30*'==')
print('Sequencia de Fibonacci')
print(30*'==')
qntt = int(input('Quantos termos voce quer mostrar? '))
print(20*'-=')
print(f'{pn} -> {sn} -> ', end='')
while tm < qntt:
    tn = pn + sn
    pn = sn
    sn = tn
    print(f'{tn} -> ', end='')
    tm += 1
print('FIM!')
print(20*'-=')
