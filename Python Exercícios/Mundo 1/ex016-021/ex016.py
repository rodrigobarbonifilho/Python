# coding=utf-8
# import math

# Meu jeito

num = float(input('Coloque aqui um numero e iremos mostrar a parte inteira dele ele: '))
print('\033[31mO numero {} tem sua parte inteira de:{}\033[m'.format(num, round(num)))

'''print()

# Jeito que acho que era pra fazer
num = float(input('Coloque aqui um numero e iremos arrendondar ele: '))
print('O numero {} arredondado para:'.format(num))
print('Cima ficará {}'.format(math.ceil(num)))
print('Baixo ficará {}'.format(math.floor(num)))

print()

# Jeito que ERA pra fazer

from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado {} tem a sua porção inteira de:{}'.format(num, trunc(num)))

# Jeito sem modulo
num = float(input('Digite aqui um valor: '))
print('O valor {} te a sua porção inteira de:{}'.format(num, int(num)))'''
