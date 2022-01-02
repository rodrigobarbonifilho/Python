# coding=utf-8
print('Informe abaixo dois numeros e irei soma-los:')
n1 = int(input('Coloque aqui um numero: '))
n2 = int(input('Coloque aqui outro numero: '))

soma = n1 + n2

print('\033[1;34mA soma de {} com {} é igual a:{}\033[m'.format(n1, n2, soma))
