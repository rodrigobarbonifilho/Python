print(40 * '\033[1;36m-=\033[m')
print('''\033[31mAnalisador de Triangulos\033[m.''')
print(40 * '\033[1;36m-=\033[m')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo  segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('\033[1;32mOs segmentos acima PODEM FORMAR um triangulo,', end=' ')
    if s1 == s2 == s3:
        print('EQUILATERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:  # Poderia ter feito assim "if s1 == s2 or s2 == s3 or s3 == s1:"
        print('ISOSCELES')
else:
    print('\033[1;31mOs segmentos acima NAO PODEM FORMAR um triangulo!\033[m')
