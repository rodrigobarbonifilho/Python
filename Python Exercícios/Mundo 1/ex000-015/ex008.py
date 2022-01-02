# coding=utf-8
d = float(input('Coloque uma distancia em metros:'))
print('A medida de {:.1f}m corresponde à:'.format(d))
print('\033[4;33m{}Km'.format(d/1000))
print('{}Hm'.format(d/100))
print('{}Dam'.format(d/10))
print('{}Dm'.format(d*10))
print('{}Cm'.format(d*100))
print('{}Mm\033[m'.format(d*1000))
