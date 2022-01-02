from math import radians, sin, cos, tan
angulo = float(input('Coloque aqui um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print()

print('\033[1;36mO angulo {:.2f} tem o SENO de:{:.2f}'.format(angulo, seno))
print('O angulo {:.2f} tem o COSSENO de:{:.2f}'.format(angulo, cosseno))
print('O angulo {:.2f} tem o TANGENTE de {:.2f}\033[m'.format(angulo, tangente))
