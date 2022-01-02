num = int(input('Digite aqui um numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print()
print('\033[4;36mAnalisando numero {}...'.format(num))
print('Milhar: {}'.format(m))
print('Centenas: {}'.format(c))
print('Dezenas: {}'.format(d))
print('Unidades: {}\033[m'.format(u))
