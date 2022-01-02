print(20 * '\033[1;34m-=\033[m')
print('Analisador de triangulos!!')
print(20 * '\033[1;34m-=\033[m')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('\033[1;33mOs Segmento acima PODEM formar um triangulo\033[m')
else:
    print('\033[1;31mOs Segmento acima NAO PODEM formar um triangulo\033[m')
