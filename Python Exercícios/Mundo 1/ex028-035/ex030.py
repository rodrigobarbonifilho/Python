# coding=utf-8
n1 = int(input('Me diga um numero qualquer: '))
if n1 % 2 == 0:
    print('\033[1;31mO numero {} é PAR\033[m'.format(n1))
else:
    print('\033[1;31mO numero {} é IMPAR\033[m'.format(n1))
