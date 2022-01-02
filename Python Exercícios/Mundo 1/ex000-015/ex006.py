# Meu Jeito

n1 = int(input('Coloque aqui um numero:'))

d = n1 * 2
t = n1 * 3
rq = n1 ** (1/2)

print('\033[1;31mO dobro de {} vale:{}'.format(n1, d))
print('O triplo de {} vale:{}'.format(n1, t))
print('A raiz quadrada de {} vale:{:.2f}\033[m'.format(n1, rq))

print()

# Jeito Guanabara

n1 = int(input('Coloque aqui um numero:'))

print('\033[1;31mO dobro de {} vale:{}'.format(n1, (n1*2)))
print('O triplo de {} vale:{}'.format(n1, (n1*3)))
print('A raiz quadrada de {} vale:{:.2f}\033[m'.format(n1, n1**(1/2)))
