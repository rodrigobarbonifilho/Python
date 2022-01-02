# hipotenusa^2 = cateto_oposto^2 + cateto_adjacente^2
# Jeito Dificil

cateto_oposto = float(input('Coloque aqui a medida do cateto oposto do triangulo retangulo: '))
cateto_adjacente = float(input('Coloque aqui a medida do cateto adjacente do triangulo retangulo: '))

quadrado_da_hipotenusa = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = quadrado_da_hipotenusa ** (1 / 2)

print('\033[4;32mA hipotenusa desse triangulo retangulo tem a medida de {:.2f}\033[m'.format(hipotenusa))

# Jeito Facil
'''from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))'''
