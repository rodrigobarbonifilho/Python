# coding=utf-8
dia = float(input('Quantos dias alugados:'))
Km = float(input('Quantos Km rodados: '))

custo_dia = dia * 60.00
custo_Km = Km * 00.15

total = custo_dia + custo_Km

print('\033[1;31mO total a pagar é de R${:.2f}\033[m'.format(total))
